import inspect
import json
import os
from typing import Any
from typing import Dict

from .exceptions import InvalidArgumentException

DEFAULTS = {
    'token': '',
}

CONFIG_FILE = 'config.json'


def _load() -> Dict[str, Any]:
    try:
        with open(CONFIG_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def _dump(cfg: Dict[str, Any]) -> None:
    with open(CONFIG_FILE, 'w') as f:
        json.dump(cfg, f, indent=4)


def get(key: str) -> str:
    cfg = _load()
    if key in cfg:
        return cfg[key]
    elif key in os.environ:
        cfg[key] = os.environ[key]
    elif key in DEFAULTS:
        # Lock in the default value if we use it.
        cfg[key] = DEFAULTS[key]

        # If default value is a function, call it.
        if inspect.isfunction(cfg[key]):
            cfg[key] = cfg[key]()
    else:
        raise InvalidArgumentException(
            f'No default or other configuration value available for {key}',
        )

    print('CONFIG: {}={}'.format(key, cfg[key]))
    _dump(cfg)
    return cfg[key]


def write(key: str, value: str) -> str:
    cfg = _load()

    cfg[key] = value

    print('CONFIG: {}={}'.format(key, cfg[key]))
    _dump(cfg)
    return cfg[key]
