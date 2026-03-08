# FIR Filter Automation using Jinja

Automates Verilog code generation for Finite Impulse Response (FIR) filters using the Jinja templating engine. Specify your filter coefficients and get clean, optimized Verilog ready for FPGA or ASIC implementation.

---

## Features

- Generates Verilog code for FIR filter designs automatically
- Jinja-based templating for flexible, readable code generation
- Excel integration for coefficient input via `xlwings`
- Detects duplicate coefficients and optimizes the output to reduce redundant operations
- Organized package structure with setup tools, templates, and examples

---

## Project Structure

```
FIR-Filter-Automation/
├── src/
│   ├── __init__.py
│   └── FIR.py                 # Main FIR generation module
├── templates/
│   ├── mcshm16_fp.v           # Multiplier module
│   ├── mprecomputer.v         # Pre-computation module
│   ├── regss.v                # Register module
│   ├── adder32.v              # 32-bit adder
│   └── ...                    # Other Verilog modules
├── examples/
│   └── example_usage.py
├── docs/
├── main.py
├── setup.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.7+
- `jinja2`
- `xlwings` (Excel integration)
- `numpy`, `pandas`

---

## Installation

**Option 1 — Install as a package**
```bash
git clone https://github.com/Mayan10/fir-filter-automation.git
cd fir-filter-automation
pip install -e .
```

**Option 2 — Dependencies only**
```bash
git clone https://github.com/Mayan10/fir-filter-automation.git
cd fir-filter-automation
pip install -r requirements.txt
```

---

## Usage

**Quick start**
```bash
python main.py
```

**From Python**
```python
from src.FIR import generate_fir_verilog

generate_fir_verilog()
```

**Run the example**
```bash
python examples/example_usage.py
```

---

## How It Works

1. **Coefficient processing** — Reads FIR filter coefficients and identifies duplicates
2. **Template rendering** — Jinja fills the Verilog template with the processed coefficients
3. **Optimization** — Duplicate coefficients are consolidated to minimize redundant logic
4. **Code generation** — Final Verilog is written to `final.v`

The generated output includes configurable FIR logic, pipelined register stages, optimized multiplier modules (`mcshm16_fp`), and accumulation adders.

---

## Planned Enhancements

- IIR filter support
- GUI for parameter input
- CSV coefficient input
- Verification testbenches
- Multi-architecture FPGA support

---

## Author

**Mayan Sharma**
GitHub: [@Mayan10](https://github.com/Mayan10)

---

## License

This project is licensed under the MIT License.
