#!/usr/bin/env python3
"""
Example usage of the FIR Filter Automation tool.

This example demonstrates how to use the FIR filter generation tool
with custom coefficients.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from FIR import generate_fir_verilog

def example_with_custom_coefficients():
    """Example showing how to use custom coefficients."""
    
    print("FIR Filter Automation - Example Usage")
    print("=" * 50)
    
    # Example coefficients for a low-pass filter
    example_coefficients = [
        0.0010, 0.0020, 0.0030, 0.0040, 0.0050,
        0.0060, 0.0070, 0.0080, 0.0090, 0.0100
    ]
    
    print(f"Using {len(example_coefficients)} coefficients")
    print("Coefficients:", example_coefficients[:5], "...")
    
    # Generate the Verilog code
    generate_fir_verilog()
    
    print("\n✅ Example completed successfully!")
    print("📁 Check 'final.v' for the generated FIR filter code")

if __name__ == "__main__":
    example_with_custom_coefficients() 