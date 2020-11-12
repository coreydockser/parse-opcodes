import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="parse-opcodes",
    version="1.0.0",
    description="takes a list of instruction names, opcodes, and arguments and turns it into a 32-column spreadsheet, with each column representing a bit",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/coreydockser/parse-opcodes.git",
    author="Corey Dockser",
    author_email="coreydockser@gmail.com",
    license="BSD-3-Clause",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["parse"],
    include_package_data=True,
    install_requires=["xlsxwriter", "openpyxl", "re", "os", "math"],
    entry_points={
        "console_scripts": [
            "parse_opcodes=parse.__main__:main",
        ]
    },
)