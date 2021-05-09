#
# Copyright (c) 2021 Info-Com Systems Pty Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
allowable_modules = ['oc311.com.github.openshift.api.', 'oc311.io.k8s.']
reject_class = ['BaseModel', 'Event', 'TokenRequest']
accept_files = [version +'.', 'resource.', 'intstr.']
for root, dirs, files in os.walk('oc311'):
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