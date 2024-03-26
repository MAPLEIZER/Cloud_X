#! /usr/bin/env python3
from setuptools import setup

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name                =   "cloudx",
    version             =   '1.0',
    description         =   "A Multi-Tool Web Vulnerability Scanner.",
    url                 =   "https://github.com/MAPLEIZER/Cloud_X.git",
    author              =   "sh4nx0r",
    py_modules          =   ['rapidscan',],
    install_requires    =   [],
    python_requires=">=3.6",
)
