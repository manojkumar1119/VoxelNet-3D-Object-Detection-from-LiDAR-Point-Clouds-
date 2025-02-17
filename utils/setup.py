#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='box overlaps',
    ext_modules=cythonize('./utils/box_overlaps.pyx')
)
