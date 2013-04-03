#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'mssqlcon',
]

requires = [
    'pyodbc',
]

setup(
    name='mssqlcon',
    version='0.1.0',
    description='Easy MSSQL python connection',
    long_description=open('README.md').read(),
    author='Jack LaBarba',
    author_email='jlabarba@plos.org',
    url='https://github.com/PLOS-Web/mssqlcon',
    packages=packages,
    package_dir={'mssqlcon': 'mssqlcon'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE.txt').read(),
    zip_safe=True,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
