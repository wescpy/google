# Google Cloud Run (GCR) code samples

## Introduction
This folder is for all [Google Cloud Run](https://cloud.google.com/cloudrun) standalone samples (meaning no other Google products (APIs, platforms, etc.) featured in a primary way:

## "Hello World!" sample app repo folders
1. [Python (2 & 3)](/cloud/cloudrun/python) (recommend 3.9+)
1. [Node.js](/cloud/cloudrun/nodejs) (recommend 16+)

Cloud Run is the GCP serverless platform for _app-hosting_. This folder contains developer code samples from the [post covering how to deploy a "Hello World!" sample app to Cloud Run](https://dev.to/wescpy/guide-to-modern-app-hosting-without-servers-on-google-cloud-37n8). The post is posted as part of the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy). The samples are available in Python and Node.js/JavaScript.

## Cost: billing required (but free?!?)
While many Google products are free to use, GCP products are not. In order to run the sample apps, you must [enable billing](http://console.cloud.google.com/billing) and have active billing supported by a financial instrument like a [credit card](https://cloud.google.com/cloudrun/docs/standard/payment-instrument) ([payment method depends on region/currency](https://support.google.com/paymentscenter/answer/9001356?ref_topic=9023854#allowed-methods)). If you're new to GCP, review the [billing and onboarding guide](https://cloud.google.com/billing/docs/onboarding-checklist). Billing wasn't required to use Cloud Run in the past, but [that changed in late 2019](https://cloud.google.com/cloudrun/docs/standard/payment-instrument).

The good news is that Cloud Run (and other GCP products) have an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits), a free daily or monthly usage before incurring charges. The Cloud Run [pricing](https://cloud.google.com/cloudrun/pricing) and [quotas](https://cloud.google.com/cloudrun/quotas) pages have more information. Furthermore, deploying to GCP serverless platforms incur [minor build and storage costs](https://cloud.google.com/cloudrun/pricing#pricing-for-related-google-cloud-products).

[Cloud Build](https://cloud.google.com/build/pricing) has its own free quota as does [Cloud Storage](https://cloud.google.com/storage/pricing#cloud-storage-always-free) (GCS). For greater transparency, Cloud Build builds your application image which is than sent to the Cloud [Container Registry](https://cloud.google.com/container-registry/pricing) or [Artifact Registry](https://cloud.google.com/artifact-registry/pricing), its successor. Storage of that image uses up some of that GCS quota as does network egress when transferring that image to the service you're deploying to. However you may live in region that does not have a free tier, so monitor storage usage to minimize potential costs. (Check out storage use and delete old/unwanted build artifacts via the [GCS browser](https://console.cloud.google.com/storage/browser).)

With the above said, you may qualify for GCP credits to offset any costs of using GCP. If you are a startup, consider applying for the [Google Cloud for Startups](https://cloud.google.com/startup) program grants. If you are a higher education student, faculty member, researcher, or are an education technology ("edtech") company, explore all the [Google Cloud for education programs](https://cloud.google.com/edu).
