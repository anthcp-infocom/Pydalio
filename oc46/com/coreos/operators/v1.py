# generated by datamodel-codegen:
#   filename:  openapi-v2.json
#   timestamp: 2021-04-29T07:54:09+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, conint, constr

from ....io.k8s.apimachinery.pkg.apis.meta import v1


class MatchExpression(BaseModel):
    key: str = Field(
        ..., description='key is the label key that the selector applies to.'
    )
    operator: str = Field(
        ...,
        description="operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.",
    )
    values: Optional[List[str]] = Field(
        None,
        description='values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.',
    )


class LabelSelector(BaseModel):
    matchExpressions: Optional[List[MatchExpression]] = Field(
        None,
        description='matchExpressions is a list of label selector requirements. The requirements are ANDed.',
    )
    matchLabels: Optional[Dict[str, str]] = Field(
        None,
        description='matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.',
    )


class Condition(BaseModel):
    lastTransitionTime: Optional[datetime] = Field(
        None,
        description='Last time the condition transitioned from one status to another.',
    )
    lastUpdateTime: Optional[datetime] = Field(
        None, description='Last time the condition was probed'
    )
    message: Optional[str] = Field(
        None,
        description='A human readable message indicating details about the transition.',
    )
    reason: Optional[str] = Field(
        None, description="The reason for the condition's last transition."
    )
    status: str = Field(
        ..., description='Status of the condition, one of True, False, Unknown.'
    )
    type: str = Field(..., description='Type of condition.')


class Ref(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    conditions: Optional[List[Condition]] = Field(
        None, description='Conditions represents the latest state of the component.'
    )
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class Components(BaseModel):
    labelSelector: LabelSelector = Field(
        ...,
        description="LabelSelector is a label query over a set of resources used to select the operator's components",
    )
    refs: Optional[List[Ref]] = Field(
        None,
        description="Refs are a set of references to the operator's component resources, selected with LabelSelector.",
    )


class Status(BaseModel):
    components: Optional[Components] = Field(
        None, description='Components describes resources that compose the operator.'
    )


class StatusModel(Enum):
    True_ = 'True'
    False_ = 'False'
    Unknown = 'Unknown'


class Override(BaseModel):
    lastTransitionTime: Optional[datetime] = Field(
        None,
        description='lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.',
    )
    message: constr(max_length=32768) = Field(
        ...,
        description='message is a human readable message indicating details about the transition. This may be an empty string.',
    )
    observedGeneration: Optional[conint(ge=0)] = Field(
        None,
        description='observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.',
    )
    reason: constr(
        regex=r'^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$', min_length=1, max_length=1024
    ) = Field(
        ...,
        description="reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.",
    )
    status: StatusModel = Field(
        ..., description='status of the condition, one of True, False, Unknown.'
    )
    type: constr(
        regex=r'^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$',
        max_length=316,
    ) = Field(
        ...,
        description='type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)',
    )


class Spec(BaseModel):
    deployments: Optional[List[str]] = None
    overrides: Optional[List[Override]] = None
    serviceAccounts: Optional[List[str]] = None


class StatusModel1(Enum):
    True_ = 'True'
    False_ = 'False'
    Unknown = 'Unknown'


class ConditionModel(BaseModel):
    lastTransitionTime: datetime = Field(
        ...,
        description='lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.',
    )
    message: constr(max_length=32768) = Field(
        ...,
        description='message is a human readable message indicating details about the transition. This may be an empty string.',
    )
    observedGeneration: Optional[conint(ge=0)] = Field(
        None,
        description='observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.',
    )
    reason: constr(
        regex=r'^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$', min_length=1, max_length=1024
    ) = Field(
        ...,
        description="reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.",
    )
    status: StatusModel1 = Field(
        ..., description='status of the condition, one of True, False, Unknown.'
    )
    type: constr(
        regex=r'^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$',
        max_length=316,
    ) = Field(
        ...,
        description='type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)',
    )


class StatusModel2(BaseModel):
    conditions: Optional[List[ConditionModel]] = None


class MatchExpressionModel(BaseModel):
    key: str = Field(
        ..., description='key is the label key that the selector applies to.'
    )
    operator: str = Field(
        ...,
        description="operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.",
    )
    values: Optional[List[str]] = Field(
        None,
        description='values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.',
    )


class Selector(BaseModel):
    matchExpressions: Optional[List[MatchExpressionModel]] = Field(
        None,
        description='matchExpressions is a list of label selector requirements. The requirements are ANDed.',
    )
    matchLabels: Optional[Dict[str, str]] = Field(
        None,
        description='matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.',
    )


class SpecModel(BaseModel):
    selector: Optional[Selector] = Field(
        None, description="Selector selects the OperatorGroup's target namespaces."
    )
    serviceAccountName: Optional[str] = Field(
        None,
        description='ServiceAccountName is the admin specified service account which will be used to deploy operator(s) in this operator group.',
    )
    staticProvidedAPIs: Optional[bool] = Field(
        None,
        description="Static tells OLM not to update the OperatorGroup's providedAPIs annotation",
    )
    targetNamespaces: Optional[List[str]] = Field(
        None,
        description='TargetNamespaces is an explicit set of namespaces to target. If it is set, Selector is ignored.',
    )


class ServiceAccountRef(BaseModel):
    apiVersion: Optional[str] = Field(None, description='API version of the referent.')
    fieldPath: Optional[str] = Field(
        None,
        description='If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. TODO: this design is not final and this field is subject to change in the future.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    name: Optional[str] = Field(
        None,
        description='Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names',
    )
    namespace: Optional[str] = Field(
        None,
        description='Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/',
    )
    resourceVersion: Optional[str] = Field(
        None,
        description='Specific resourceVersion to which this reference is made, if any. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency',
    )
    uid: Optional[str] = Field(
        None,
        description='UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids',
    )


class StatusModel3(BaseModel):
    lastUpdated: datetime = Field(
        ...,
        description="LastUpdated is a timestamp of the last time the OperatorGroup's status was Updated.",
    )
    namespaces: Optional[List[str]] = Field(
        None,
        description='Namespaces is the set of target namespaces for the OperatorGroup.',
    )
    serviceAccountRef: Optional[ServiceAccountRef] = Field(
        None,
        description='ServiceAccountRef references the service account object specified.',
    )


class Operator(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMetaV2] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[Dict[str, Any]] = Field(
        None, description='OperatorSpec defines the desired state of Operator'
    )
    status: Optional[Status] = Field(
        None,
        description='OperatorStatus defines the observed state of an Operator and its components',
    )


class OperatorCondition(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: v1.ObjectMetaV2 = Field(
        ...,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[Spec] = Field(
        None,
        description='OperatorConditionSpec allows a cluster admin to convey information about the state of an operator to OLM, potentially overriding state reported by the operator.',
    )
    status: Optional[StatusModel2] = Field(
        None,
        description='OperatorConditionStatus allows an operator to convey information its state to OLM. The status may trail the actual state of a system.',
    )


class OperatorConditionList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[OperatorCondition] = Field(
        ...,
        description='List of operatorconditions. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class OperatorGroup(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: v1.ObjectMetaV2 = Field(
        ...,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[SpecModel] = Field(
        None, description='OperatorGroupSpec is the spec for an OperatorGroup resource.'
    )
    status: Optional[StatusModel3] = Field(
        None,
        description='OperatorGroupStatus is the status for an OperatorGroupResource.',
    )


class OperatorGroupList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[OperatorGroup] = Field(
        ...,
        description='List of operatorgroups. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )


class OperatorList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Operator] = Field(
        ...,
        description='List of operators. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )