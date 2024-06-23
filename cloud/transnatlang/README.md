# Google Cloud Natural Language & Translation APIs code samples

These are the code samples found in the language-oriented post covering both GCP APIs (_coming soon_).

## Code samples
App | Platform | Credentials | Client libraries | Auth libraries
--- | --- | --- | ---
[`transnatlang-svcacct-gcp.py`](transnatlang-svcacct-gcp.py) | Python | ADC (service account or OAuth client ID) | Product | Current/new
[`transnatlang-svcacct-gcp.js`](transnatlang-svcacct-gcp.js) | Node.js (CommonJS) | ADC (service account or OAuth client ID) | Product | Current/new
[`transnatlang-svcacct-gcp.mjs`](transnatlang-svcacct-gcp.mjs) | Node.js (modern JS/ECMAScript module) | ADC (service account or OAuth client ID) | Product | Current/new
[`transnatlang-apikey-old.py`](transnatlang-apikey-old.py) | Python | API key | Platform | Old

_Product_ client libraries are those created for each (GCP) product whereas the [original _platform_ client libraries](https://developers.google.com/api-client-library) are meant to support Google APIs from multiple product families. By default, these client libraries use Application Default Credentials (ADC) to access GCP APIs. Depending on the execution environment, ADC will either point to service account or OAuth client ID credentials.

## Running the samples
To learn the code and run the sample scripts from the blog post in your development environment, you're more likely to use the latter credentials type (OAuth client ID) by running the `gcloud auth application-default login` command to obtain user authorized credentials. When you're ready to move towards production and want to switch to impersonating a service account, you'd run the `gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL` command. Learn more at the ADC pages in the docs, starting with the [ADC setup page](https://cloud.google.com/docs/authentication/provide-credentials-adc). Also see the [page on the different authentication methods and credentials types](https://cloud.google.com/docs/authentication).

While API keys are the easiest of all the credentials to get started with and implement, they are the least secure of all three credentials types used by Google APIs, so support for API keys isn't always complete (because their use is generally not recommended). The platform client library and older auth libraries are required for the **API key** version of the sample app because API keys are unsupported by the Python [Translation API (product) client libraries](https://cloud.google.com/translate/docs/setup#installing_client_libraries) even though they _are_ [supported by the Python Natural Language API (product) client library](https://cloud.google.com/docs/authentication/api-keys#using-with-client-libs). (**NOTE**: API key support in the Node.js (product or platform) client libraries is unknown -- if anyone has a working example, please file an issue and submit a PR.)
