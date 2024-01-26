# Python App Engine
## "Hello World!" sample app

This is the GAE "Hello World!" sample app for Python developers; there is another [folder for Node.js developers](/cloud/appengine/nodejs).


## Prerequisites

- A Google account and Cloud (GCP) project with an active billing account
- Familiarity with operating system terminal/shell commands
- General skills in Python 3.x and a web framework like Flask, etc.
- [Currently supported versions of Python](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python)


## Cost

App Engine, along with all the other GCP products, are not free services. While you may not have enabled billing in App Engine's early days, [all applications now require an active billing account](https://cloud.google.com/appengine/docs/standard/payment-instrument) backed by a financial instrument (usually a credit card). Don't worry, App Engine (and other GCP products) still have an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits) and as long as you stay within those limits, you won't incur any charges. Also check the App Engine [pricing](https://cloud.google.com/appengine/pricing) and [quotas](https://cloud.google.com/appengine/quotas) pages for more information.

Furthermore, deploying to GCP serverless platforms incur [minor build and storage costs](https://cloud.google.com/appengine/pricing#pricing-for-related-google-cloud-products). [Cloud Build](https://cloud.google.com/build/pricing) has its own free quota as does [Cloud Storage](https://cloud.google.com/storage/pricing#cloud-storage-always-free). For greater transparency, Cloud Build builds your application image which is than sent to the [Cloud Container Registry](https://cloud.google.com/container-registry/pricing), or [Artifact Registry](https://cloud.google.com/artifact-registry/pricing), its successor; storage of that image uses up some of that (Cloud Storage) quota as does network egress when transferring that image to the service you're deploying to. However you may live in region that does not have such a free tier, so be aware of your storage usage to minimize potential costs. (You may look at what storage you're using and how much, including deleting build artifacts via [your Cloud Storage browser](https://console.cloud.google.com/storage/browser).)

With the above said, you may qualify for GCP credits to offset any costs of using GCP. If you are a startup, consider applying for the [Google Cloud for Startups](https://cloud.google.com/startup) program grants. If you are a higher education student, faculty member, researcher, or are an education technology ("edtech") company, explore all the [Google Cloud for education programs](https://cloud.google.com/edu).


### Table of contents

If there is a logical codelab to do immediately after completing one, they will be designated as NEXT. Other recommended codelabs will be listed as RECOMMENDED, and the more optional ones will be labeled as OTHERS (and usually in some kind of priority order).


## Community

Python App Engine developers hang out in various online communities, including these:
- [Slack](https://googlecloud-community.slack.com) (`#app-engine`, `#python`, and other channels); visit [this link](https://join.slack.com/t/googlecloud-community/shared_invite/zt-ywj8ieuc-BrAaHC~qe5IgelXS9vzNRA) to join
- [Reddit](http://reddit.com) in the [Google Cloud](https://reddit.com/googlecloud) or [App Engine](https://reddit.com/appengine) subs (subReddits).
- [App Engine mailing list](http://groups.google.com/group/google-appengine)


## References

- Python App Engine
    - [App Engine 1st vs. 2nd generation runtimes](https://cloud.google.com/appengine/docs/standard/runtimes)
    - [Python 2 App Engine (Standard) runtime](https://cloud.google.com/appengine/docs/standard/python/runtime)
    - [Python 3 App Engine (Standard) runtime](https://cloud.google.com/appengine/docs/standard/python3/runtime)
    - [Python App Engine (Flexible)](https://cloud.google.com/appengine/docs/flexible/python)

- Google Cloud Platform (GCP)
    - [Python on GCP](https://cloud.google.com/python)
    - [Cloud client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)
    - [All GCP documentation](https://cloud.google.com/docs)

