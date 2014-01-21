#!/usr/bin/env python
import sys
if sys.version < '3':
    from distutils.command.build_py import build_py
else:
    from distutils.command.build_py import build_py_2to3 as build_py

from distutils.core import setup

setup(
    cmdclass        = {'build_py': build_py},
    name            = 'logstash-forwarder',
    version         = '1.0',
    description     = 'Redis-based log forwarder for Logstash',
    author          = 'Michael Stella',
    author_email    = 'michael@jwplayer.com',
    scripts         = ['logstash-forwarder'],
    requires        = ['redis', 'pyinotify'],
)

