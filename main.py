#!/usr/bin/env python3
"""
FIR Filter Automation - Main Script

This script generates Verilog code for FIR filters using Jinja templating.
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from FIR import generate_fir_verilog

def main():
    """Main function to run the FIR filter generation."""
    try:
        print("FIR Filter Automation Tool")
        print("=" * 40)
        
        # Generate the Verilog code
        generate_fir_verilog()
        
        print("\n✅ Verilog code generated successfully!")
        print("📁 Check 'final.v' for the generated FIR filter code")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 