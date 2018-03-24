import inspect
import json
import os
import random
import string

from .exceptions import InvalidArgumentException

DEFAULTS = {
    "token": "",
}

def get(key: str) -> str:
    try:
        cfg = json.load(open('config.json'))
    except FileNotFoundError:
        cfg = {}
    if key in cfg:
        return cfg[key]
    elif key in os.environ:
        cfg[key] = os.environ[key]
    elif key in DEFAULTS:
        # Lock in the default value if we use it.
        cfg[key] = DEFAULTS[key]

        if inspect.isfunction(cfg[key]): # If default value is a function, call it.
            cfg[key] = cfg[key]()
    else:
        raise InvalidArgumentException('No default or other configuration value available for {key}'.format(key=key))

    print("CONFIG: {0}={1}".format(key, cfg[key]))
    fh = open('config.json', 'w')
    fh.write(json.dumps(cfg, indent=4))
    return cfg[key]

def write(key: str, value: str) -> str:
    try:
        cfg = json.load(open('config.json'))
    except FileNotFoundError:
        cfg = {}

    cfg[key] = value

    print("CONFIG: {0}={1}".format(key, cfg[key]))
    fh = open('config.json', 'w')
    fh.write(json.dumps(cfg, indent=4, sort_keys=True))
    return cfg[key]
