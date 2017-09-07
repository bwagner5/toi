#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Command

long_description = """
This utility converts Terraform output to json or key-value format to be passed into terraform as a tfvars file or packer as json
"""

setup(
    name = 'toi',
    version = '1.0.0',
    license='MIT',
    description = 'Converts terraform output to key/vals or json',
    long_description=long_description,
    author = 'Brandon Wagner',
    maintainer = 'Brandon Wagner',
    py_modules = [],
    scripts = ['toi'],
    zip_safe = True,
    install_requires=[]
)
