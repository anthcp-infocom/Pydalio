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

from oc311.v1 import *
      

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
            class_path = globals()[class_type]
            try:
                my_class = globals()[class_type].parse_obj(doc)
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


to = validate(partial(RouteTargetReference, kind = 'Service', name = 'fred'))
print (get_yaml(to))

routespec = validate(partial(RouteSpec, host = 'hello', to = to ))

x = validate(partial(Route, apiVersion = 'v1', kind = 'Route', spec = routespec ))

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
docs = load_full_yaml('examples/Pod.yml')
# docs = load_full_yaml('examples/test_route.yaml')
for doc in docs:
    print (get_obj_src(doc))
for doc in docs:
    print (get_yaml(doc))

# test obj source
print("testing python object source...")
print()
pod = Pod(apiVersion='v1', kind='Pod', metadata=ObjectMeta(annotations=None, clusterName=None, creationTimestamp=None, deletionGracePeriodSeconds=None, deletionTimestamp=None, finalizers=None, generateName=None, generation=None, initializers=None, labels={'mylabelname': 'myqueueapp'}, name='just-a-queue', namespace=None, ownerReferences=None, resourceVersion=None, selfLink=None, uid=None), spec=PodSpec(activeDeadlineSeconds=None, affinity=None, automountServiceAccountToken=None, containers=[Container(args=None, command=None, env=None, envFrom=None, image='richardchesterwood/k8s-fleetman-queue:release1', imagePullPolicy=None, lifecycle=None, livenessProbe=None, name='queue-app-container', ports=None, readinessProbe=None, resources=None, securityContext=None, stdin=None, stdinOnce=None, terminationMessagePath=None, terminationMessagePolicy=None, tty=None, volumeDevices=None, volumeMounts=None, workingDir=None)], dnsConfig=None, dnsPolicy=None, hostAliases=None, hostIPC=None, hostNetwork=None, hostPID=None, hostname=None, imagePullSecrets=None, initContainers=None, nodeName=None, nodeSelector=None, priority=None, priorityClassName=None, readinessGates=None, restartPolicy=None, schedulerName=None, securityContext=None, serviceAccount=None, serviceAccountName=None, shareProcessNamespace=None, subdomain=None, terminationGracePeriodSeconds=None, tolerations=None, volumes=None), status=None)
print (get_yaml(pod))