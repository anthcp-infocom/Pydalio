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
from functools import partial

from oc311.v1 import *
# from oc46.v1 import *
from generate import *   

# example on how to construct a python route object
# validating will allow the object to say what is missing if incorrect.
to = validate(partial(RouteTargetReference, kind = 'Service', name = 'fred'))
routespec = validate(partial(RouteSpec, host = 'hello', to = to ))
route_obj = validate(partial(Route, apiVersion = 'v1', kind = 'Route', spec = routespec ))

# show Openshift Json output
print (get_json(route_obj))
# show Openshift yaml output
print (get_yaml(route_obj))

# This example shows how to read a openshift yaml file and then using Pydantic's parse_obj to create a
# openshift Route object. Trapping any errors will show details as to why the parse failed
y = load_yaml('examples/test_route.yaml')
try:
    r = Route.parse_obj(y)
except ValidationError as e:
    print(e.json())

print (get_yaml(r))
# This shows how to print the Openshift Object source so you can get the python object creation "code"
print (get_obj_src(r))

# load_full_yaml() will parse a single pyaml file with multiple objects separated by "---""
# docs = load_full_yaml('examples/multi-ext.yaml')
docs = load_full_yaml(globals(),'examples/Pod.yml')
# docs = load_full_yaml('examples/test_route.yaml')
for doc in docs:
    print (get_obj_src(doc))
for doc in docs:
    print (get_yaml(doc))

# This shows how a Python Pod objectt can be constructed...
print("testing python object source...")
print()
pod = Pod(apiVersion='v1', kind='Pod', metadata=ObjectMeta(annotations=None, clusterName=None, creationTimestamp=None, deletionGracePeriodSeconds=None, deletionTimestamp=None, finalizers=None, generateName=None, generation=None, initializers=None, labels={'mylabelname': 'myqueueapp'}, name='just-a-queue', namespace=None, ownerReferences=None, resourceVersion=None, selfLink=None, uid=None), spec=PodSpec(activeDeadlineSeconds=None, affinity=None, automountServiceAccountToken=None, containers=[Container(args=None, command=None, env=None, envFrom=None, image='richardchesterwood/k8s-fleetman-queue:release1', imagePullPolicy=None, lifecycle=None, livenessProbe=None, name='queue-app-container', ports=None, readinessProbe=None, resources=None, securityContext=None, stdin=None, stdinOnce=None, terminationMessagePath=None, terminationMessagePolicy=None, tty=None, volumeDevices=None, volumeMounts=None, workingDir=None)], dnsConfig=None, dnsPolicy=None, hostAliases=None, hostIPC=None, hostNetwork=None, hostPID=None, hostname=None, imagePullSecrets=None, initContainers=None, nodeName=None, nodeSelector=None, priority=None, priorityClassName=None, readinessGates=None, restartPolicy=None, schedulerName=None, securityContext=None, serviceAccount=None, serviceAccountName=None, shareProcessNamespace=None, subdomain=None, terminationGracePeriodSeconds=None, tolerations=None, volumes=None), status=None)
print (get_yaml(pod))