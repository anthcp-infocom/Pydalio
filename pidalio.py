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
from pydoc import locate       

sys.path.append('.')
from oc311.com.github.openshift.api.route.v1 import *
from oc311.io.k8s.api.core.v1 import *
import importlib, inspect, pkgutil

from importlib import import_module
from pkgutil import iter_modules, walk_packages
from pathlib import Path
from functools import partial

import oc311


# globals()['modules'] = {}

# # iterate through the modules in the current package
# #package_dir = Path(__file__).resolve().parent
# for root, dirs, files in os.walk('model'):
#         for diry in dirs:
#             dirpath = os.path.join(root, diry)
#             for (_, module_name, _) in iter_modules([dirpath]):
#                 module_path = dirpath.replace('/','.') + '.' + module_name
#                 print (module_path, module_name)
#                 try:
#                     globals()['modules'][module_path] = import_module(module_path)
#                 except:
#                     pass

allowable_modules = ['oc311.com.github.openshift.api.', 'oc311.io.k8s.api.']
reject_class = ['BaseModel', 'Event', 'TokenRequest']
mod_oc_reg = {}
mod_k8_reg = {}

def get_modules_in_package(package_name: str, version: str):
    for root, dirs, files in os.walk(package_name):
        for filename in files:
            # print(os.path.join(root, filename))
            if filename == '__init__.py' or filename[-3:] != '.py' or filename.find(version + '.'):
                continue
            modname = os.path.join(root, filename)[:-3].replace('/','.')
            res = [ele for ele in allowable_modules if(ele in modname )]
            res_str = "".join(res)
            if not bool(res):
                continue
            if modname:
                #print(res, filename, modname)
                try:
                    liblist = inspect.getmembers(importlib.import_module(modname), inspect.isclass)
                except:
                    pass
                else:
                    for name in inspect.getmembers(importlib.import_module(modname), inspect.isclass):
                        #print(name[0], modname)
                        resA = any(ele in name[0] for ele in reject_class)
                        if not resA:
                            if 'openshift' in res_str:
                                if name[0] not in mod_oc_reg:
                                    mod_oc_reg[name[0]] = modname
                                else:
                                    raise KeyError("Key {} already exists in oc".format(name[0]))
                            elif 'k8s' in res_str:
                                if name[0] not in mod_k8_reg:
                                    mod_k8_reg[name[0]] = modname
                                else:
                                    raise KeyError("Key {} already exists in k8s".format(name[0]))

    return
            

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
 

def load_full_yaml(filename):
    docs = []
    with open(filename, 'r') as stream:
        for doc in yaml.safe_load_all(stream):
            class_type = doc['kind']
            if mod_oc_reg.get(class_type):
                class_path = mod_oc_reg[class_type]
            elif mod_k8_reg.get(class_type):
                class_path = mod_k8_reg[class_type]
            else:
                print('Class {} not found'.format(class_type))
                continue
            try:
                my_class = locate(class_path + '.' + class_type).parse_obj(doc)
            except ValidationError as e:
                print(e.json())
            else:
                docs.append(my_class)
    return docs

def validate(f):
    try:
        x = f()
    except ValidationError as e:
        print(e.json())
    return x

version = 'v1'
get_modules_in_package('oc311', version)

to = validate(partial(RouteTargetReference, kind = 'Service', name = 'fred'))
print (get_yaml(to))

# try:
#     to = RouteTargetReference(kind = 'Service', name = 'fred')
# except ValidationError as e:
#     print(e.json())

routespec = validate(partial(RouteSpec, host = 'hello', to = to ))

# try:
#     routespec = RouteSpec(host = 'hello', to = to )
# except ValidationError as e:
#     print(e.json())

x = validate(partial(Route, apiVersion = 'v1', kind = 'Route', spec = routespec ))

# try:
#     x = Route(apiVersion = 'v1', kind = 'Route', spec = routespec )
# except ValidationError as e:
#     print(e.json())

print (get_json(x))
print (get_yaml(x))

# y = load_yaml('examples/test_route.yaml')
# try:
#     r = Route.parse_obj(y)
# except ValidationError as e:
#     print(e.json())

# print (get_yaml(r))
# print (get_obj_src(r))

# docs = load_full_yaml('examples/multi-ext.yaml')
# docs = load_full_yaml('examples/Pod.yml')
docs = load_full_yaml('examples/test_route.yaml')
for doc in docs:
    print (get_obj_src(doc))
for doc in docs:
    print (get_yaml(doc))