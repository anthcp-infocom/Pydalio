## Pydalio ( pythonic variation on the greek word for "rudder", following the K8s nautical theme)

This code is pre-alpha, started on April 25th 2021 and was inspired by Hikaru and Pulumi.
Since the idea is to use Python as a devops scripting language ( instead of a programming language), I have taken a miminalist offline approach as I dont like the online requirement for Pulumi from a security perspective.
So convert your yamls into python object code and then create a new .py module with your new openshift python objects etc.

Why create Pydalio? Having to put up with poor debugging options in Helm, and finding out that there was no global variables in go template as used by Helm was the last straw. It appears this is by design (which is fair enough!) e.g I guess the golang logic is its time to use golang instead of go templates if you reach this point in Helm...
Not for me. I decided a long time ago if you cant debug a computer lang by "single stepping", forget it so goodbye Helm!

So I wondered how far Python and Pydantic could be used, and as it turns out they have very broad shoulders indeed and now you can code your Openshift resources as python objects...

This code supports OpenShift YAML "validation" but the source openapi info for OpenShift 3.11 appears to have errors from a validation perspective. e.g OpenShift 3.11 Route object has "status" as not optional. Anyway I have fixed it here and v4.6 is fine.

There is no reason why it could be used on K8s alone but my focus at the moment is OpenShift 3.11 & 4.6 as it pays the bills.

I have a few more ideas on Pydalio's development...
1. Add Openshift K8s Rest code so you can create and delete K8s objects as part of a pipeline.
2. Create a helm library to python module converter...
3. Create usage pipeline frameworks for GitLab, GitHub etc
4. Add report generation as the "jobs not finished till the paperwork is done"!
5. Maybe a K8s object GUI editor?
6. Add Strimizi to the Python object library
7. Add in AWS boto3 and Azure control libs..
8. Any other ideas?

Anthony, 
Technical Director,
Info-com Systems Pty Ltd