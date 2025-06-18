#!/usr/bin/env python
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
cosy-py=cosy_lexers:CosyPythonLexer
'''

setup(
    name='cosy_lexers',
    version='0.0.1',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.0'
    ],
    zip_safe=True,
)