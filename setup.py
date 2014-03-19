#!/usr/bin/env python
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name            = 'logstash-tools',
    version         = '1.0',
    description     = 'A collection of tools for use with logstash',
    long_description= open('README').read(),
    url             = 'https://github.com/JWPlayer/logstash-tools',
    author          = 'Michael Stella',
    author_email    = 'michael@jwplayer.com',
    scripts         = ['logfile-forwarder'],
    install_requires= ['redis', 'pyinotify'],
    classifiers     = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ]
)

