#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pytest>=3.0.3',
    'tinydb>=3.2.1',
    'requests>=2.12.4',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='stf_selector',
    version='0.1.0',
    description="stf devices stf_selector",
    long_description=readme + '\n\n' + history,
    author="Juan Liu",
    author_email='littlewei_liu@163.com',
    url='https://github.com/wliu_intern/stf_selector',
    packages=[
        'stf_selector',
    ],
    package_dir={'stf_selector':
                 'stf_selector'},
    entry_points={
        'console_scripts': [
            'stf_selector=stf_selector.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='stf_selector',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
