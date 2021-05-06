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
from inspect import isclass

from oc311.v1 import *
from generate import *   

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