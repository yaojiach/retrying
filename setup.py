#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

settings = dict()

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet',
    'Topic :: Utilities',
]

with open('README.rst') as file_readme:
    readme = file_readme.read()

with open('HISTORY.rst') as file_history:
    history = file_history.read()

settings.update(
    name='retrying',
    version='1.3.4-dev',
    description='Retrying',
    long_description=readme + '\n\n' + history,
    author='Ray Holder',
    license='Apache 2.0',
    url='https://github.com/rholder/retrying',
    classifiers=CLASSIFIERS,
    keywords="decorator decorators retry retrying exception exponential backoff",
    py_modules= ['retrying'],
    test_suite="test_retrying"
)

setup(**settings)
