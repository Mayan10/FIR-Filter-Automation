import jinja2 as jj
try:
    import xlwings as xw
    XLWINGS_AVAILABLE = True
except ImportError:
    XLWINGS_AVAILABLE = False
    print("Note: xlwings not available. Excel integration disabled.")

from pathlib import Path

def generate_fir_verilog():
    """Generate FIR filter Verilog code using Jinja templating."""

    # FIR coefficients
    coefficients = [
        0.0218, 0.0731, -0.0383, -0.1470, 0.0033, 0.2816, 0.1117, -0.4417,
        -0.3661, 0.0573, 0.0808, -0.0576, -0.1454, 0.0307, 0.2259, 0.0406,
        -0.3083, -0.00017203, 0.00036743, 0.00037300, -0.3665, -0.00063921,
        0.2608, 0.9459, -0.0000047150, -0.0012, -0.0004375, 0.0015, 0.0011,
        -0.0015, -0.0019, 0.0012, 0.0028, -0.0005, -0.0037, -0.0006,
        0.0043, 0.0023, -0.0045, -0.0044, 0.0040, 0.0067, -0.0026,
        -0.0090, 0.0000, 0.0110, 0.0038, -0.0120, -0.0087, 0.0116,
        0.0147, -0.0092, -0.0214, 0.0040, 0.0284, 0.0050, -0.0352,
        -0.0195, 0.0412, 0.0438, -0.0460, -0.0936, 0.0490, 0.3140,
        0.4500, 0.3140, 0.0490, -0.0936, -0.0460, 0.0438, 0.0412,
        -0.0195, -0.0352, 0.0050, 0.0284, 0.0040, -0.0214, -0.0092,
        0.0147, 0.0116, -0.0087, -0.0120, 0.0038, 0.0110, 0.000016049,
        -0.0090, -0.0026, 0.0067, 0.0040, -0.0044, -0.0045, 0.0023,
        0.0043, -0.0006, -0.0037, -0.0005, -0.0028, 0.0012, -0.0019,
        -0.0015, 0.0011, 0.0015, -0.0004, -0.0012, -0.0047, 0.9459,
        0.2608, -6.3921e-04, -0.00036651, 0.00037300, 0.00036743,
        -0.00017203, -0.00030832, 0.000040569, 0.00022586, 0.000030667,
        -0.00014539, -0.5763, 0.000080783, 0.000057334, -0.000036611,
        -0.4417, 0.000011167, 0.000028159, 0.00000033368, -0.1470,
        -0.0000038274, 0.7307
    ]

    num_coefficients = len(coefficients)

    def group_coefficients(input_list):
        """
        Groups coefficients by value.
        Each group contains indices of identical coefficients.
        """
        groups = {}
        for idx, val in enumerate(input_list):
            groups.setdefault(val, []).append(idx)
        return list(groups.values())

    groups = group_coefficients(coefficients)
    num_unique_coeffs = len(groups)

    verilog_template = r'''
module fir_mcshm8(clk, rst, x, {% for i in range(1, num_coefficients + 1) %}b{{ i }},{% endfor %}cf);
input clk, rst;
input [31:0] x;
input [31:0]{% for i in range(1, num_coefficients) %}b{{i}},{% endfor %}b{{num_coefficients}};
output [31:0] cf;

wire [31:0] coutf[1:{{num_coefficients}}];
wire [31:0] cadd[3:{{num_coefficients+1}}];
wire [27:0] x1,x2,x3,x4,x5,x6;
wire [31:0] rout[2:{{num_coefficients}}];

wire [8:0] exx;
wire [23:0] a1;
wire as;

assign exx = x[31:23];
assign as  = (8'b0 || x[30:23]);
assign a1  = {as, x[22:0]};

mprecomputer p1(a1, x1, x2, x3, x4, x5, x6);

{% for g in groups %}
{% set base = g[0] + 1 %}
mcshm16_fp f{{ loop.index }}(x1,x2,x3,x4,x5,x6,exx,b{{base}},coutf[{{base}}]);
{% endfor %}

{% for g in groups %}
{% set base = g[0] + 1 %}
{% for idx in g[1:] %}
assign coutf[{{idx+1}}] = coutf[{{base}}];
{% endfor %}
{% endfor %}

regss r{{num_coefficients}}(clk, rst, coutf[{{num_coefficients}}], rout[{{num_coefficients}}]);
adder32 a{{num_coefficients}}(coutf[{{num_coefficients-1}}], rout[{{num_coefficients}}], cadd[{{num_coefficients+1}}], rst);

{% for i in range(num_coefficients, 2, -1) %}
regss r{{i-1}}(clk, rst, cadd[{{i+1}}], rout[{{i-1}}]);
adder32 a{{i-1}}(coutf[{{i-2}}], rout[{{i-1}}], cadd[{{i}}], rst);
{% endfor %}

assign cf = cadd[3];
endmodule
'''

    template = jj.Template(verilog_template)
    rendered_verilog = template.render(
        num_coefficients=num_coefficients,
        groups=groups
    )

    # Write output
    output_path = Path(__file__).parent.parent / "final.v"
    with open(output_path, "w") as f:
        f.write(rendered_verilog)

    repeated = sum(1 for g in groups if len(g) > 1)
    unique = sum(1 for g in groups if len(g) == 1)

    print("FIR Optimization Report")
    print("=" * 30)
    for g in groups:
        if len(g) > 1:
            print("Shared multiplier for taps:", [i+1 for i in g])

    print("\nUnique coefficient count :", unique)
    print("Repeated coefficient groups :", repeated)
    print("Total multipliers used :", num_unique_coeffs)
    print("Total taps :", num_coefficients)


if __name__ == "__main__":
    generate_fir_verilog()
