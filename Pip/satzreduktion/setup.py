#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'flair']

setup_requirements = []

test_requirements = []

setup(
    author="Gruppe-4-2",
    author_email='nw20hewo@studserv.uni-leipzig.de',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Satzreduktion mithilfe von NER Tools",
    entry_points={
        'console_scripts': [
            'satzreduktion=satzreduktion.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='satzreduktion',
    name='satzreduktion',
    packages=find_packages(include=['satzreduktion']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://git.informatik.uni-leipzig.de/nw20hewo/satz-reduktion',
    version='0.1.12',
    zip_safe=False,
)
