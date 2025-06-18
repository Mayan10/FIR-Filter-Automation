# FIR Filter Automation using Jinja

This project automates the generation of Verilog code for a Finite Impulse Response (FIR) filter using the Jinja templating engine. It allows for flexible handling of filter coefficients and generates efficient Verilog code that can be used in FPGA or ASIC design.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Verilog Template](#verilog-template)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Introduction
This project aims to automate the generation of FIR filter Verilog code using Jinja. The automation allows users to specify the filter coefficients and generate the corresponding Verilog code, streamlining the design process.

## Features
- Automatically generates Verilog code for FIR filter design
- Uses Jinja templating for flexible code generation
- Supports Excel integration for coefficient input
- Detects duplicate coefficients for optimized Verilog code generation
- Proper Python package structure with setup tools
- Organized project structure with templates and examples

## Project Structure
```
FIR-Filter-Automation/
├── src/                    # Python source code
│   ├── __init__.py        # Package initialization
│   └── FIR.py             # Main FIR generation module
├── templates/              # Verilog template files
│   ├── mcshm16_fp.v       # Multiplier module
│   ├── mprecomputer.v     # Pre-computation module
│   ├── regss.v            # Register module
│   ├── adder32.v          # 32-bit adder
│   └── ...                # Other Verilog modules
├── examples/               # Usage examples
│   └── example_usage.py   # Example script
├── docs/                   # Documentation
├── main.py                 # Main execution script
├── setup.py               # Package setup
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── .github/attributes    # GitHub language detection
└── README.md             # This file
```

## Requirements
- Python 3.7+
- `jinja2` package
- `xlwings` package (for Excel integration)
- `numpy` and `pandas` (for data handling)

## Installation

### Option 1: Install as a package
```bash
# Clone the repository
git clone https://github.com/your-username/fir-filter-automation.git
cd fir-filter-automation

# Install the package
pip install -e .
```

### Option 2: Install dependencies only
```bash
# Clone the repository
git clone https://github.com/your-username/fir-filter-automation.git
cd fir-filter-automation

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Quick Start
```bash
# Run the main script
python main.py
```

### Using the Python Module
```python
from src.FIR import generate_fir_verilog

# Generate FIR filter Verilog code
generate_fir_verilog()
```

### Example Usage
```bash
# Run the example
python examples/example_usage.py
```

## Verilog Template
The generated Verilog code is based on a template that includes:
- FIR filter implementation with configurable coefficients
- Optimized multiplier modules (mcshm16_fp)
- Register stages for pipelining
- Adder modules for accumulation
- Duplicate coefficient detection and optimization

## How It Works
1. **Coefficient Processing**: The script processes FIR filter coefficients and detects duplicates
2. **Template Rendering**: Uses Jinja to render the Verilog code template with the given coefficients
3. **Optimization**: Detects duplicate coefficients and optimizes the Verilog code to minimize redundant operations
4. **Code Generation**: Outputs the final Verilog code to `final.v`

## Future Enhancements
- Add support for more filter types (e.g., IIR)
- Integrate graphical user interface (GUI) for easier parameter input
- Expand coefficient input options to other file formats (e.g., CSV)
- Add verification testbenches
- Support for different FPGA architectures

## License 
This project is licensed under the MIT License.
