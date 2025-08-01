import logging
import tomllib
import pprint
from collections import OrderedDict
from pathlib import Path
from .system_config import SystemConfig

__all__ = ['load_config', 'print_config']

def load_config(path: Path) -> SystemConfig:
    """ load input toml"""
    try:
        with open(path, "rb") as f:
            config_date=tomllib.load(f)
            return SystemConfig(**config_date)
    except FileNotFoundError:
        logging.error(f"File {path} not found")
        raise
    except tomllib.TOMLDecodeError as e:
        logging.error(f"File {path} error : {e}")
        raise

def print_config(config: dict) -> None:
    #custom_order = ['system', 'theory', 'potential', 'solver', 'basis']
    #ordered_config = OrderedDict()
    #for key in custom_order:
    #    ordered_config[key] = config[key]
    # pprint.pprint(ordered_config)
    pprint.pprint(config)
