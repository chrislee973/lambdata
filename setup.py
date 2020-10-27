import setuptools


# Required packages
REQUIRED = ["numpy", "pandas"]

# Grabs description from README as our long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-christopherlee973", # Replace with your own username
    version="0.0.3", # First version - change in subsequent versions
    author="chrislee973", # Replace with your own username
    description="A collection of data science functions", # Short description
    long_description=long_description, # Long description - from README
    long_description_content_type="text/markdown", # Explains type of format long description has
    url="https://github.com/chrislee973/lambdata", # Where the package code is located
    packages=setuptools.find_packages(),
    install_requires=REQUIRED, # Required dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6' # Version of python we are running
)
