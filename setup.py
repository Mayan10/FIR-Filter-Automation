from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fir-filter-automation",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Automated Verilog code generation for FIR filters using Jinja templating",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/fir-filter-automation",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "": ["templates/*.v"],
    },
) 