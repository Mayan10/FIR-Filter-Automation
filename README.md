# FIR Filter Automation using Jinja

This project automates the generation of Verilog code for a Finite Impulse Response (FIR) filter using the Jinja templating engine. It allows for flexible handling of filter coefficients and generates efficient Verilog code that can be used in FPGA or ASIC design.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Verilog Template](#verilog-template)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Introduction
This project aims to automate the generation of FIR filter Verilog code using Jinja. The automation allows users to specify the filter coefficients in an Excel sheet and generate the corresponding Verilog code, streamlining the design process.

## Features
- Automatically generates Verilog code for FIR filter design.
- Uses Jinja templating for flexible code generation.
- Supports Excel integration for coefficient input.
- Detects duplicate coefficients for optimized Verilog code generation.

## Requirements
- Python 3.x
- `jinja2` package
- `xlwings` package
- Excel file with the filter coefficients

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
2. Install the required Python packages:
   ```pip install jinja2 xlwings```

## Usage
1. Update the Excel file with your filter coefficients.
2. Modify the Python script to specify the correct Excel file and range for coefficients.
3. Run the script to generate the final.v Verilog file:
   ```python generate_fir_verilog.py```

## Verilog Template
The generated Verilog code is based on a template, which can be modified to suit different design needs. The template handles FIR filter implementation, coefficient assignment, and modular structure.

## How It Works
1. Reading the Coefficients: The script uses xlwings to read FIR filter coefficients from an Excel file.
2. Template Rendering: It uses Jinja to render the Verilog code template with the given coefficients.
3. Duplicate Detection: The script detects duplicate coefficients and optimizes the Verilog code to minimize redundant operations.

## Future Enhancements
- Add support for more filter types (e.g., IIR).
- Integrate graphical user interface (GUI) for easier parameter input.
- Expand coefficient input options to other file formats (e.g., CSV).

## License 
This project is licensed under the MIT License.
