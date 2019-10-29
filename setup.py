#!/usr/bin/env python

import setuptools

from pathlib import Path

ROOT = Path(__file__).parent

with open(f'{ROOT}/README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='fireREST',
    version='0.0.1',
    author='Oliver Kaiser',
    author_email='oliver.kaiser@outlook.com',
    description='Wrapper for Cisco Firepower Management Center REST API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kaisero/fireREST.git',
    packages=setuptools.find_packages(),
    install_requires=['PyYAML', 'requests', 'urllib3'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX',
    ],
)
