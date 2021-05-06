
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

from importlib import import_module
from pkgutil import iter_modules, walk_packages
from pathlib import Path
from functools import partial
from inspect import isclass


version = 'v1'
allowable_modules = ['oc46.com.github.openshift.api.', 'oc46.io.k8s.']
reject_class = ['BaseModel', 'Event', 'TokenRequest']
accept_files = [version +'.', 'resource.', 'intstr.']
for root, dirs, files in os.walk('oc46'):
    for filename in files:
        # if filename == '__init__.py' or filename[-3:] != '.py' or filename.find(version + '.'):
        if filename == '__init__.py' or filename[-3:] != '.py' or not [ele for ele in accept_files if(ele in filename )]:
            continue
        modname = os.path.join(root, filename)[:-3].replace('/','.')
        res = [ele for ele in allowable_modules if(ele in modname )]
        if not bool(res) or not modname:
            continue
        try:
            module = import_module(modname)
        except:
            pass
        else:
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isclass(attribute):            
                    # Add the class to this package's variables
                    globals()[attribute_name] = attribute