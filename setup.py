from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

VERSION = '0.0.1'
DESCRIPTION = 'A computational approach tool to predict Head and Neck Cancer affected patients from their single cell RNA seq data.'
LONG_DESCRIPTION = (this_directory/"README.md").read_text()

# Setting up
setup(
    name="HNSCPred",
    version=VERSION,
    author="Akanksha Jarwal and Aman Srivastava",
    author_email="<akanksha20331@iiitd.ac.in>",
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas','numpy','tensorflow','keras',],
    keywords=['python', 'Head and neck cancer', 'Diagnosis', 'Single cell', 'Genomics'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    license_files= 'LICENSE.txt'
)
