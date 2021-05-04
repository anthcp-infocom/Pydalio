## Pidalio ( Greek for Rudder, following the K8s nautical theme)

This code is pre-alpha, started on April 25th 2021 and was inspired by Hikaru and Pulumi.

I wondered how far Pydantic could be used, and as it turns out has very broad shoulders indeed!

This code supports OpenShift YAML validation but the source openapi info for OpenShift 3.11 appears to have errors from a validation perspective. e.g OpenShift 3.11 Route object has "status" as not optional!

There is no reason why it could be used on K8s alone but my focus at the moment is OpenShift 3.11 & 4.6.

Anthony, 
Technical Director,
Info-com Systems Pty Ltd