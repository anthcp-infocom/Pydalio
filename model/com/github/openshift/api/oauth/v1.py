# generated by datamodel-codegen:
#   filename:  openapi-v2.json
#   timestamp: 2021-04-29T07:54:09+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ......io.k8s.apimachinery.pkg.apis.meta import v1


class ClusterRoleScopeRestriction(BaseModel):
    allowEscalation: bool = Field(
        ...,
        description='AllowEscalation indicates whether you can request roles and their escalating resources',
    )
    namespaces: List[str] = Field(
        ...,
        description='Namespaces is the list of namespaces that can be referenced.  * means any of them (including *)',
    )
    roleNames: List[str] = Field(
        ...,
        description='RoleNames is the list of cluster roles that can referenced.  * means anything',
    )


class ScopeRestriction(BaseModel):
    clusterRole: Optional[ClusterRoleScopeRestriction] = Field(
        None,
        description='ClusterRole describes a set of restrictions for cluster role scoping.',
    )
    literals: Optional[List[str]] = Field(
        None,
        description='ExactValues means the scope has to match a particular set of strings exactly',
    )


class OAuthAccessToken(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    authorizeToken: Optional[str] = Field(
        None, description='AuthorizeToken contains the token that authorized this token'
    )
    clientName: Optional[str] = Field(
        None, description='ClientName references the client that created this token.'
    )
    expiresIn: Optional[int] = Field(
        None,
        description='ExpiresIn is the seconds from CreationTime before this token expires.',
    )
    inactivityTimeoutSeconds: Optional[int] = Field(
        None,
        description='InactivityTimeoutSeconds is the value in seconds, from the CreationTimestamp, after which this token can no longer be used. The value is automatically incremented when the token is used.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    redirectURI: Optional[str] = Field(
        None, description='RedirectURI is the redirection associated with the token.'
    )
    refreshToken: Optional[str] = Field(
        None,
        description='RefreshToken is the value by which this token can be renewed. Can be blank.',
    )
    scopes: Optional[List[str]] = Field(
        None, description='Scopes is an array of the requested scopes.'
    )
    userName: Optional[str] = Field(
        None, description='UserName is the user name associated with this token'
    )
    userUID: Optional[str] = Field(
        None, description='UserUID is the unique UID associated with this token'
    )


class OAuthAccessTokenList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[OAuthAccessToken] = Field(
        ..., description='Items is the list of OAuth access tokens'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None


class OAuthAuthorizeToken(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    clientName: Optional[str] = Field(
        None, description='ClientName references the client that created this token.'
    )
    codeChallenge: Optional[str] = Field(
        None,
        description='CodeChallenge is the optional code_challenge associated with this authorization code, as described in rfc7636',
    )
    codeChallengeMethod: Optional[str] = Field(
        None,
        description='CodeChallengeMethod is the optional code_challenge_method associated with this authorization code, as described in rfc7636',
    )
    expiresIn: Optional[int] = Field(
        None,
        description='ExpiresIn is the seconds from CreationTime before this token expires.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    redirectURI: Optional[str] = Field(
        None, description='RedirectURI is the redirection associated with the token.'
    )
    scopes: Optional[List[str]] = Field(
        None, description='Scopes is an array of the requested scopes.'
    )
    state: Optional[str] = Field(None, description='State data from request')
    userName: Optional[str] = Field(
        None, description='UserName is the user name associated with this token'
    )
    userUID: Optional[str] = Field(
        None,
        description='UserUID is the unique UID associated with this token. UserUID and UserName must both match for this token to be valid.',
    )


class OAuthAuthorizeTokenList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[OAuthAuthorizeToken] = Field(
        ..., description='Items is the list of OAuth authorization tokens'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None


class OAuthClient(BaseModel):
    accessTokenInactivityTimeoutSeconds: Optional[int] = Field(
        None,
        description='AccessTokenInactivityTimeoutSeconds overrides the default token inactivity timeout for tokens granted to this client. The value represents the maximum amount of time that can occur between consecutive uses of the token. Tokens become invalid if they are not used within this temporal window. The user will need to acquire a new token to regain access once a token times out. This value needs to be set only if the default set in configuration is not appropriate for this client. Valid values are: - 0: Tokens for this client never time out - X: Tokens time out if there is no activity for X seconds The current minimum allowed value for X is 300 (5 minutes)',
    )
    accessTokenMaxAgeSeconds: Optional[int] = Field(
        None,
        description='AccessTokenMaxAgeSeconds overrides the default access token max age for tokens granted to this client. 0 means no expiration.',
    )
    additionalSecrets: Optional[List[str]] = Field(
        None,
        description='AdditionalSecrets holds other secrets that may be used to identify the client.  This is useful for rotation and for service account token validation',
    )
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    grantMethod: Optional[str] = Field(
        None,
        description='GrantMethod is a required field which determines how to handle grants for this client. Valid grant handling methods are:\n - auto:   always approves grant requests, useful for trusted clients\n - prompt: prompts the end user for approval of grant requests, useful for third-party clients',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    redirectURIs: Optional[List[str]] = Field(
        None,
        description='RedirectURIs is the valid redirection URIs associated with a client',
    )
    respondWithChallenges: Optional[bool] = Field(
        None,
        description='RespondWithChallenges indicates whether the client wants authentication needed responses made in the form of challenges instead of redirects',
    )
    scopeRestrictions: Optional[List[ScopeRestriction]] = Field(
        None,
        description='ScopeRestrictions describes which scopes this client can request.  Each requested scope is checked against each restriction.  If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied.',
    )
    secret: Optional[str] = Field(
        None, description='Secret is the unique secret associated with a client'
    )


class OAuthClientAuthorization(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    clientName: Optional[str] = Field(
        None,
        description='ClientName references the client that created this authorization',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    scopes: Optional[List[str]] = Field(
        None, description='Scopes is an array of the granted scopes.'
    )
    userName: Optional[str] = Field(
        None, description='UserName is the user name that authorized this client'
    )
    userUID: Optional[str] = Field(
        None,
        description='UserUID is the unique UID associated with this authorization. UserUID and UserName must both match for this authorization to be valid.',
    )


class OAuthClientAuthorizationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[OAuthClientAuthorization] = Field(
        ..., description='Items is the list of OAuth client authorizations'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None


class OAuthClientList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[OAuthClient] = Field(
        ..., description='Items is the list of OAuth clients'
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None


class UserOAuthAccessToken(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    authorizeToken: Optional[str] = Field(
        None, description='AuthorizeToken contains the token that authorized this token'
    )
    clientName: Optional[str] = Field(
        None, description='ClientName references the client that created this token.'
    )
    expiresIn: Optional[int] = Field(
        None,
        description='ExpiresIn is the seconds from CreationTime before this token expires.',
    )
    inactivityTimeoutSeconds: Optional[int] = Field(
        None,
        description='InactivityTimeoutSeconds is the value in seconds, from the CreationTimestamp, after which this token can no longer be used. The value is automatically incremented when the token is used.',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = None
    redirectURI: Optional[str] = Field(
        None, description='RedirectURI is the redirection associated with the token.'
    )
    refreshToken: Optional[str] = Field(
        None,
        description='RefreshToken is the value by which this token can be renewed. Can be blank.',
    )
    scopes: Optional[List[str]] = Field(
        None, description='Scopes is an array of the requested scopes.'
    )
    userName: Optional[str] = Field(
        None, description='UserName is the user name associated with this token'
    )
    userUID: Optional[str] = Field(
        None, description='UserUID is the unique UID associated with this token'
    )


class UserOAuthAccessTokenList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[UserOAuthAccessToken]
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = None
