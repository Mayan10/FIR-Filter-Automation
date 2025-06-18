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
    
    # Coefficients (you can modify this to read from Excel)
    # To use Excel integration, uncomment the following lines:
    # if XLWINGS_AVAILABLE:
    #     wb = xw.Book('BookName.xlsm')
    #     sht = wb.sheets['SheetName']
    #     coefficients = sht.range('enter_column_range').value
    # else:
    #     coefficients = [default_coefficients]
    
    coefficients = [0.0218, 0.0731, -0.0383, -0.1470, 0.0033, 0.2816, 0.1117, -0.4417, -0.3661, 0.0573, 0.0808, -0.0576, -0.1454, 0.0307, 0.2259, 0.0406, -0.3083, -0.00017203,0.00036743,0.00037300, -0.3665, -0.00063921, 0.2608, 0.9459, -0.0000047150, -0.0012, -0.0004375, 0.0015, 0.0011, -0.0015, -0.0019, 0.0012, 0.0028, -0.0005, -0.0037, -0.0006, 0.0043, 0.0023, -0.0045, -0.0044, 0.0040, 0.0067, -0.0026, -0.0090, 0.0000, 0.0110, 0.0038, -0.0120, -0.0087, 0.0116, 0.0147, -0.0092, -0.0214, 0.0040, 0.0284, 0.0050, -0.0352, -0.0195, 0.0412, 0.0438, -0.0460, -0.0936, 0.0490, 0.3140, 0.4500, 0.3140, 0.0490, -0.0936, -0.0460, 0.0438, 0.0412, -0.0195, -0.0352, 0.0050, 0.0284, 0.0040, -0.0214, -0.0092, 0.0147, 0.0116, -0.0087, -0.0120, 0.0038, 0.0110, 0.000016049, -0.0090, -0.0026, 0.0067, 0.0040, -0.0044, -0.0045, 0.0023, 0.0043, -0.0006, -0.0037, -0.0005, -0.0028, 0.0012, -0.0019, -0.0015, 0.0011, 0.0015, -0.0004, -0.0012, -0.0047, 0.9459, 0.2608, -6.3921e-04, -0.00036651, 0.00037300, 0.00036743, -0.00017203, -0.00030832, 0.000040569, 0.00022586, 0.000030667, -0.00014539, -0.5763, 0.000080783, 0.000057334, -0.000036611, -0.4417, 0.000011167, 0.000028159, 0.00000033368, -0.1470, -0.0000038274, 0.7307]
    num_coefficients = len(coefficients)

    def find_unique_and_duplicates_with_indices(input_list):
        # Dictionary to store element counts and their indices
        element_info = {}
        
        # Loop through each element in the input list
        for index, element in enumerate(input_list):
            # If the element is already in the dictionary, append the new index
            if element in element_info:
                element_info[element]['count'] += 1
                element_info[element]['indices'].append(index)
            # If the element is not in the dictionary, add it with count 1 and current index
            else:
                element_info[element] = {'count': 1, 'indices': [index]}
        
        # Lists to store unique elements and duplicates with indices
        unique_elements = []
        duplicates_with_indices = []
        
        # Loop through the dictionary to separate unique elements and duplicates
        for element, info in element_info.items():
            if info['count'] == 0:
                unique_elements.append(element)
            else:
                duplicates_with_indices.append((element, info['indices']))
        
        return duplicates_with_indices

    m = find_unique_and_duplicates_with_indices(coefficients)
    l = len(m)

    verilog_template = '''module fir_mcshm8(clk, rst, x, {% for i in range(1, num_coefficients + 1) %}b{{ i }},{% endfor %}cf);
input clk, rst;
input [31:0] x;
input [31:0]{% for i in range(1, num_coefficients) %}b{{i}},{% endfor %}b{{num_coefficients}};
output [31:0] cf
wire [31:0]coutf[1:{{num_coefficients}}];

wire [31:0]cadd[3:{{num_coefficients+1}}];
wire [27:0]x1,x2,x3,x4,x5,x6;
wire [31:0]rout[2:{{num_coefficients}}];

wire [8:0]exx;
wire [23:0]a1;
wire [23:0]b11;
wire as;


assign exx=x[31:23];
assign as=(8'b0 || x[30:23]);
//assign bs=(8'b0 || bin[30:23]);

assign  a1[23:0]={as,x[22:0]};
//assign  b11[23:0]={bs,bin[22:0]};

mprecomputer p1(a1,x1,x2,x3,x4,x5,x6);
{% for i in range(1,l+1) %}
{% set kk = m[i-1][1][0]+1 %}
mcshm16_fp f{{ i }}(x1,x2,x3,x4,x5,x6,exx,b{{kk}},coutf[{{kk}}]);
{% endfor %}
{% for i in range(0,l) %}{% for j in range(1,m[i][1]|length) %}{% set rep = m[i][1][j]+1 %}{% set by = m[i][1][0]+1 %}
assign coutf[{{rep}}] = coutf[{{by}}];{% endfor %}{% endfor %}

regss r{{num_coefficients}}(clk,rst,coutf[{{num_coefficients}}],rout[{{num_coefficients}}]);   
adder32 a{{num_coefficients}}(coutf[{{num_coefficients-1}}],rout[{{num_coefficients}}],cadd[{{num_coefficients+1}}],rst); 
{% for i in range(num_coefficients,2,-1) %}
regss r{{i-1}}(clk,rst,cadd[{{i+1}}],rout[{{i-1}}]);   
adder32 a{{i-1}}(coutf[{{i-2}}],rout[{{i-1}}],cadd[{{i}}],rst);
{% endfor %}
assign cf=cadd[3];
endmodule
'''

    template = jj.Template(verilog_template)
    rendered_verilog = template.render(num_coefficients=num_coefficients , l = l,m = m)
    
    # Write to final.v in the project root
    output_path = Path(__file__).parent.parent / "final.v"
    with open(output_path, "w") as f:
        f.write(rendered_verilog)

    count_repeated = 0
    count_unique = 0

    for i in m:
        if len(i[1])>1:
            temp=[]
            count_repeated+=1
            for j in range(len(i[1])):
                temp.append(i[1][j]+1)
            print("the repeated coefficient indices are",temp)
            temp.clear()

    for i in m:
        if(len(i[1]))<2:
            temp1=[]
            count_unique+=1
            for j in range(len(i[1])):
                temp1.append(i[1][j]+1)
            print("the non repeated coefficient index is",temp1)
            temp1.clear()

    print("the  number of coeffecients repeated:",count_repeated)
    print("the number of coeffecients not repeated:",count_unique)

if __name__ == "__main__":
    generate_fir_verilog()