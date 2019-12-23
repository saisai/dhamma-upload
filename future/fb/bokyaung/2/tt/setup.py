#!/usr/bin/env python
# coding=utf-8
import os
import re
import sys
import codecs



try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()


if sys.argv[-1] == 'test':
    try:
        __import__('py')
    except ImportError:
        print('py.test required.')
        sys.exit(1)

    errors = os.system('py.test test_tablib.py')
    sys.exit(bool(errors))
'''
packages = [
    'tablib', 'tablib.formats',
    'tablib.packages',
    'tablib.packages.dbfpy',
    'tablib.packages.dbfpy3'
]
'''

packages = [
    'crawler'
]

install = [
    'BeautifulSoup',    
]

"""
with open('tablib/core.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)
"""

here = os.path.abspath(dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='crawler',
    version='0.0.1',
    description='Get links from files',
    long_description=long_description,
    author='Sai Sai',
    author_email='saisai@gmail.com',
    url='http://saisai.org',
    packages=packages,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'crawler = crawler.cli:main',
        ],
    },
)
