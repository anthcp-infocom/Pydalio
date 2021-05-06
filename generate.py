from typing import List
from pydantic import BaseModel, ValidationError, conint
import os, sys
import yaml     
import importlib, inspect, pkgutil
from pathlib import Path
from functools import partial


def get_yaml(obj):
    return yaml.dump(obj.dict(exclude_none=True))

def get_json(obj):
    return obj.json(exclude_none=True)

def load_yaml(filename):
    with open(filename, 'r') as stream:
        try:
            x = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        print(x)
    return x

def load_yaml_all(filename):
    with open(filename, 'r') as stream:
        try:
            x = yaml.safe_load_all(stream)
        except yaml.YAMLError as exc:
            print(exc)
        print(x)
    return x

def get_obj_src(x):
    return repr(x)

def validate(f):
    try:
        x = f()
    except ValidationError as e:
        print(e.json())
    return x   