#!/usr/bin/env python

from setuptools import setup

setup(
    name='coffer_mac',
    packages=['coffer_mac'],
    version='0.1.0',
    description='Tiny Python API for performing MAC address lookups using Coffer.',
    license='MIT',
    url='https://github.com/vesche/coffer_mac',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    install_requires=['beautifulsoup4', 'requests'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Security"
    ]
)