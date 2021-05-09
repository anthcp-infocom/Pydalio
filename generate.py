#
# Copyright (c) 2021 Info-Com Systems Pty Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List
from pydantic import BaseModel, ValidationError, conint
import os, sys
import yaml     
import importlib, inspect, pkgutil
from pathlib import Path
from functools import partial

def load_full_yaml(globals, filename):
    docs = []
    with open(filename, 'r') as stream:
        for doc in yaml.safe_load_all(stream):
            class_type = doc['kind']
            # class_path = globals()[class_type]
            class_path = globals[class_type]
            try:
                my_class = globals[class_type].parse_obj(doc)
            except ValidationError as e:
                print(e.json())
            else:
                docs.append(my_class)
    return docs


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