# generated by datamodel-codegen:
#   filename:  openshift-openapi-spec.json
#   timestamp: 2021-05-02T06:23:52+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ......io.k8s.api.core import v1
from ......io.k8s.apimachinery.pkg.apis.meta import v1 as v1_1


class AllowedFlexVolume(BaseModel):
    driver: str = Field(..., description='Driver is the name of the Flexvolume driver.')


class IDRange(BaseModel):
    max: Optional[int] = Field(
        None, description='Max is the end of the range, inclusive.'
    )
    min: Optional[int] = Field(
        None, description='Min is the start of the range, inclusive.'
    )


class RunAsUserStrategyOptions(BaseModel):
    type: Optional[str] = Field(
        None,
        description='Type is the strategy that will dictate what RunAsUser is used in the SecurityContext.',
    )
    uid: Optional[int] = Field(
        None,
        description='UID is the user id that containers must run as.  Required for the MustRunAs strategy if not using namespace/service account allocated uids.',
    )
    uidRangeMax: Optional[int] = Field(
        None,
        description='UIDRangeMax defines the max value for a strategy that allocates by range.',
    )
    uidRangeMin: Optional[int] = Field(
        None,
        description='UIDRangeMin defines the min value for a strategy that allocates by range.',
    )


class SupplementalGroupsStrategyOptions(BaseModel):
    ranges: Optional[List[IDRange]] = Field(
        None,
        description='Ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end.',
    )
    type: Optional[str] = Field(
        None,
        description='Type is the strategy that will dictate what supplemental groups is used in the SecurityContext.',
    )


class FSGroupStrategyOptions(BaseModel):
    ranges: Optional[List[IDRange]] = Field(
        None,
        description='Ranges are the allowed ranges of fs groups.  If you would like to force a single fs group then supply a single range with the same start and end.',
    )
    type: Optional[str] = Field(
        None,
        description='Type is the strategy that will dictate what FSGroup is used in the SecurityContext.',
    )


class SELinuxContextStrategyOptions(BaseModel):
    seLinuxOptions: Optional[v1.SELinuxOptions] = Field(
        None, description='seLinuxOptions required to run as; required for MustRunAs'
    )
    type: Optional[str] = Field(
        None,
        description='Type is the strategy that will dictate what SELinux context is used in the SecurityContext.',
    )


class RangeAllocation(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources',
    )
    data: str = Field(
        ...,
        description='data is a byte array representing the serialized state of a range allocation.  It is a bitmap with each bit set to one to represent a range is taken.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata",
    )
    range: str = Field(
        ...,
        description='range is a string representing a unique label for a range of uids, "1000000000-2000000000/10000".',
    )


class RangeAllocationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources',
    )
    items: List[RangeAllocation] = Field(..., description='List of RangeAllocations.')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ListMeta] = Field(
        None,
        description='More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata',
    )


class SecurityContextConstraints(BaseModel):
    allowHostDirVolumePlugin: bool = Field(
        ...,
        description='AllowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin',
    )
    allowHostIPC: bool = Field(
        ...,
        description='AllowHostIPC determines if the policy allows host ipc in the containers.',
    )
    allowHostNetwork: bool = Field(
        ...,
        description='AllowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec.',
    )
    allowHostPID: bool = Field(
        ...,
        description='AllowHostPID determines if the policy allows host pid in the containers.',
    )
    allowHostPorts: bool = Field(
        ...,
        description='AllowHostPorts determines if the policy allows host ports in the containers.',
    )
    allowPrivilegeEscalation: Optional[bool] = Field(
        None,
        description='AllowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.',
    )
    allowPrivilegedContainer: bool = Field(
        ...,
        description='AllowPrivilegedContainer determines if a container can request to be run as privileged.',
    )
    allowedCapabilities: List[str] = Field(
        ...,
        description="AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities. To allow all capabilities you may use '*'.",
    )
    allowedFlexVolumes: Optional[List[AllowedFlexVolume]] = Field(
        None,
        description='AllowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the "Volumes" field.',
    )
    allowedUnsafeSysctls: Optional[List[str]] = Field(
        None,
        description='AllowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.\n\nExamples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.',
    )
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources',
    )
    defaultAddCapabilities: List[str] = Field(
        ...,
        description='DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.',
    )
    defaultAllowPrivilegeEscalation: Optional[bool] = Field(
        None,
        description='DefaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.',
    )
    forbiddenSysctls: Optional[List[str]] = Field(
        None,
        description='ForbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.\n\nExamples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.',
    )
    fsGroup: Optional[FSGroupStrategyOptions] = Field(
        None,
        description='FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.',
    )
    groups: Optional[List[str]] = Field(
        None,
        description='The groups that have permission to use this security context constraints',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata",
    )
    priority: int = Field(
        ...,
        description='Priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields.  The higher the int, the higher priority. An unset value is considered a 0 priority. If scores for multiple SCCs are equal they will be sorted from most restrictive to least restrictive. If both priorities and restrictions are equal the SCCs will be sorted by name.',
    )
    readOnlyRootFilesystem: bool = Field(
        ...,
        description='ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.',
    )
    requiredDropCapabilities: List[str] = Field(
        ...,
        description='RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.',
    )
    runAsUser: Optional[RunAsUserStrategyOptions] = Field(
        None,
        description='RunAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext.',
    )
    seLinuxContext: Optional[SELinuxContextStrategyOptions] = Field(
        None,
        description='SELinuxContext is the strategy that will dictate what labels will be set in the SecurityContext.',
    )
    seccompProfiles: Optional[List[str]] = Field(
        None,
        description="SeccompProfiles lists the allowed profiles that may be set for the pod or container's seccomp annotations.  An unset (nil) or empty value means that no profiles may be specifid by the pod or container.\tThe wildcard '*' may be used to allow all profiles.  When used to generate a value for a pod the first non-wildcard profile will be used as the default.",
    )
    supplementalGroups: Optional[SupplementalGroupsStrategyOptions] = Field(
        None,
        description='SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.',
    )
    users: Optional[List[str]] = Field(
        None,
        description='The users who have permissions to use this security context constraints',
    )
    volumes: List[str] = Field(
        ...,
        description='Volumes is a white list of allowed volume plugins.  FSType corresponds directly with the field names of a VolumeSource (azureFile, configMap, emptyDir).  To allow all volumes you may use "*". To allow no volumes, set to ["none"].',
    )


class SecurityContextConstraintsList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources',
    )
    items: List[SecurityContextConstraints] = Field(
        ..., description='List of security context constraints.'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1_1.ListMeta] = Field(
        None,
        description='More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata',
    )


class PodSecurityPolicyReviewSpec(BaseModel):
    serviceAccountNames: Optional[List[str]] = Field(
        None,
        description='serviceAccountNames is an optional set of ServiceAccounts to run the check with. If serviceAccountNames is empty, the template.spec.serviceAccountName is used, unless it\'s empty, in which case "default" is used instead. If serviceAccountNames is specified, template.spec.serviceAccountName is ignored.',
    )
    template: v1.PodTemplateSpec = Field(
        ...,
        description='template is the PodTemplateSpec to check. The template.spec.serviceAccountName field is used if serviceAccountNames is empty, unless the template.spec.serviceAccountName is empty, in which case "default" is used. If serviceAccountNames is specified, template.spec.serviceAccountName is ignored.',
    )


class PodSecurityPolicySelfSubjectReviewSpec(BaseModel):
    template: v1.PodTemplateSpec = Field(
        ..., description='template is the PodTemplateSpec to check.'
    )


class PodSecurityPolicySubjectReviewSpec(BaseModel):
    groups: Optional[List[str]] = Field(
        None, description="groups is the groups you're testing for."
    )
    template: v1.PodTemplateSpec = Field(
        ...,
        description='template is the PodTemplateSpec to check. If template.spec.serviceAccountName is empty it will not be defaulted. If its non-empty, it will be checked.',
    )
    user: Optional[str] = Field(
        None,
        description='user is the user you\'re testing for. If you specify "user" but not "group", then is it interpreted as "What if user were not a member of any groups. If user and groups are empty, then the check is performed using *only* the serviceAccountName in the template.',
    )


class PodSecurityPolicySubjectReviewStatus(BaseModel):
    allowedBy: Optional[v1.ObjectReference] = Field(
        None,
        description='allowedBy is a reference to the rule that allows the PodTemplateSpec. A rule can be a SecurityContextConstraint or a PodSecurityPolicy A `nil`, indicates that it was denied.',
    )
    reason: Optional[str] = Field(
        None,
        description='A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available.',
    )
    template: Optional[v1.PodTemplateSpec] = Field(
        None,
        description='template is the PodTemplateSpec after the defaulting is applied.',
    )


class ServiceAccountPodSecurityPolicyReviewStatus(BaseModel):
    allowedBy: Optional[v1.ObjectReference] = Field(
        None,
        description='allowedBy is a reference to the rule that allows the PodTemplateSpec. A rule can be a SecurityContextConstraint or a PodSecurityPolicy A `nil`, indicates that it was denied.',
    )
    name: str = Field(
        ..., description='name contains the allowed and the denied ServiceAccount name'
    )
    reason: Optional[str] = Field(
        None,
        description='A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available.',
    )
    template: Optional[v1.PodTemplateSpec] = Field(
        None,
        description='template is the PodTemplateSpec after the defaulting is applied.',
    )


class PodSecurityPolicyReviewStatus(BaseModel):
    allowedServiceAccounts: List[ServiceAccountPodSecurityPolicyReviewStatus] = Field(
        ...,
        description='allowedServiceAccounts returns the list of service accounts in *this* namespace that have the power to create the PodTemplateSpec.',
    )


class PodSecurityPolicySelfSubjectReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds',
    )
    spec: PodSecurityPolicySelfSubjectReviewSpec = Field(
        ...,
        description='spec defines specification the PodSecurityPolicySelfSubjectReview.',
    )
    status: Optional[PodSecurityPolicySubjectReviewStatus] = Field(
        None,
        description='status represents the current information/status for the PodSecurityPolicySelfSubjectReview.',
    )


class PodSecurityPolicySubjectReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds',
    )
    spec: PodSecurityPolicySubjectReviewSpec = Field(
        ...,
        description='spec defines specification for the PodSecurityPolicySubjectReview.',
    )
    status: Optional[PodSecurityPolicySubjectReviewStatus] = Field(
        None,
        description='status represents the current information/status for the PodSecurityPolicySubjectReview.',
    )


class PodSecurityPolicyReview(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds',
    )
    spec: PodSecurityPolicyReviewSpec = Field(
        ..., description='spec is the PodSecurityPolicy to check.'
    )
    status: Optional[PodSecurityPolicyReviewStatus] = Field(
        None,
        description='status represents the current information/status for the PodSecurityPolicyReview.',
    )
