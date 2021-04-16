#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup,find_packages
import SeedTaag
setup(
    name='SeedTaag',

    version=SeedTaag.__version__,

    packages=find_packages(),

    author='TAAG',

    description="A faire",

    long_description="A faire",

    url='https://github.com/TeamProjetM1/SeedTaag',

    entry_points={
        'console_scripts': [
            'seedtaag = SeedTagg.__main__:main',
        ],
    },
    install_requires=['networkx','python-libsbml','pandas']
)
