#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Command

long_description = """
This utility converts Terraform output to json or key-value format to be passed into terraform as a tfvars file or packer as json
"""

setup(
    name = 'toi',
    packages = ['toi'],
    version = '1.0.2',
    license='MIT',
    description = 'Converts terraform output to key/vals or json',
    long_description=long_description,
    author = 'Brandon Wagner',
    author_email = 'brandon@brandonwagner.info',
    maintainer = 'Brandon Wagner',
    url = 'https://github.com/bwagner5/toi',
    download_url = 'https://github.com/bwagner5/toi/archive/1.0.2.tar.gz',
    keywords = ['Terraform', 'Packer', 'HashiCorp'],
    zip_safe = True,
    install_requires=[]
)
