"""
Base package for logstash tools
"""
from __future__ import print_function

__author__    = 'Michael Stella <michael@jwplayer.com>'
__copyright__ = "Copyright (c) 2013-2014 Long Tail Ad Solutions"
__version__   = "1.0"

import json
import logging
import os
import redis
import sys
import time

DEFAULT_RETRY = 10

log_output=logging.getLogger('output')
log_output.setLevel(logging.WARN)

class Sink(object):
    """Output sink base class"""

    def log(self, **kwargs):
        """Overload this to log a message and handle errors"""
        pass


class StdoutSink(Sink):
    """Output to STDOUT in JSON format"""

    def log(self, **kwargs):
        """Log a message"""
        print(json.dumps(kwargs))


class RedisSink(Sink):
    """Output to Redis"""

    def __init__(self, host, key, port=6379):
        self._backoff = DEFAULT_RETRY
        self._conn = None
        self.host = host
        self.port = port
        self.key = key
        self._connect()

    def _connect(self):
        """Initiates the Redis connection"""
        log_output.info("Redis: connecting to {}:{}".format(self.host, self.port))
        self._conn = redis.StrictRedis(
                        host=self.host,
                        port=self.port,
                        db=0,
                        socket_timeout=30)
        self._conn.ping()


    def log(self, **kwargs):
        """Log a message"""
        try:
            self._conn.rpush(self.key, json.dumps(kwargs))
            self._backoff = DEFAULT_RETRY
        except redis.exceptions.RedisError as e:
            log_output.error("Redis: {}".format(e))
            time.sleep(self._backoff)
            self._backoff = self._backoff * 2

            # try to reconnect
            try:
                self._connect()
                log_output.info("Redis: reconnected to server {0}:{1}".format(self.host, self.port))
                self._conn.rpush(self.key, json.dumps(kwargs))
            except Exception as e1:
                log_output.error("Redis: {0}".format(e1))


    def ping(self):
        """Ping the server.  Boolean."""
        return self._conn.ping()


def read_config(cfgfile):
    """Read the config file"""

    cfg = {}
    inputs = []
    outputs = []

    with open(cfgfile, 'r') as f:
        try:
            cfg = json.loads(f.read())
        except ValueError as e:
            logging.error("Could not read config file: {0}".format(e))
            sys.exit(-1)

    return (cfg['input'], cfg['output'])
