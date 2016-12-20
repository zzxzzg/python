#! /usr/bin/env python3

from setuptools import setup , find_packages
setup(name='setup_test',
      version='1.0',
      packages=find_packages('src'),
      package_dir={'': 'src'},

      )