#!/usr/bin/env python

from setuptools import setup

setup(
    name            = 'logstash-tools',
    version         = '1.0.3',
    description     = 'A collection of tools for use with logstash',
    long_description= open('README').read(),
    url             = 'https://github.com/JWPlayer/logstash-tools',
    author          = 'Michael Stella',
    author_email    = 'michael@jwplayer.com',
    packages        = ['logstash'],
    scripts         = ['logfile-forwarder', 'cloudtrail-importer'],
    install_requires= ['redis', 'pyinotify'],
    classifiers     = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
    ]
)

