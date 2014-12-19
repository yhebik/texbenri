#!/usr/bin/env python3
from distutils.core import setup
setup(
    name='texbenri',
    version='0.3',
    packages=['texbenri.bundle', 'texbenri.bbl', 'texbenri.bibsub'],
    package_data={'texbenri.bibsub': ['texbenri/bibsub/refdict.dat']},
    author='Kentaro Yamamoto',
    author_email='yhebik@gmail.com',
    description='TeX benri (useful) module collection.',
    long_description='',
    url='https://github.com/yhebik/texbenri',
    )
