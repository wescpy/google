# Google Cloud Natural Language & Translation APIs code samples

These are the code samples found in the [language-oriented post](https://dev.to/wescpy/text-based-language-processing-enhanced-with-aiml-1b1h) covering both GCP APIs (_coming soon_).

## Code samples
App | Platform | Credentials | Client libraries | Auth libraries
--- | --- | --- | --- | ---
[`transnatlang-svcacct-gcp.py`](transnatlang-svcacct-gcp.py) | Python | ADC (service account or OAuth client ID) | Product | Current/new
[`transnatlang-svcacct-gcp.js`](transnatlang-svcacct-gcp.js) | Node.js (CommonJS) | ADC (service account or OAuth client ID) | Product | Current/new
[`transnatlang-svcacct-gcp.mjs`](transnatlang-svcacct-gcp.mjs) | Node.js (modern JS / ECMAScript module) | ADC (service account or OAuth client ID) | Product | Current/new
[`transnatlang-apikey-old.py`](transnatlang-apikey-old.py) | Python | API key | Platform | Old

_Product_ client libraries are those created for each (GCP) product. By default, these client libraries use Application Default Credentials (ADC) to access GCP APIs. Depending on the execution environment, ADC will either point to service account or OAuth client ID credentials.

[_Platform_ client libraries](https://developers.google.com/api-client-library) are older and meant to support Google APIs from multiple product families. The blog post features samples that primarily use the former, but the Python API key version requires use of the older platform libraries because API keys aren't fully supported by the (Python) Translation API product client library.


## Running the samples

### ADC (service account or OAuth client ID)
To learn the code and run the sample scripts from the blog post in your development environment, you're more likely to use the latter credentials type (OAuth client ID) by running the `gcloud auth application-default login` command to obtain user authorized credentials. When you're ready to move towards production and want to switch to impersonating a service account, you'd run the `gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL` command. Learn more at the ADC pages in the docs, starting with the [ADC setup page](https://cloud.google.com/docs/authentication/provide-credentials-adc). Also see the [page on the different authentication methods and credentials types](https://cloud.google.com/docs/authentication).

### API key

While API keys are the easiest of all the credentials to get started with and implement, they are the least secure of all three credentials types used by Google APIs, so support for API keys isn't always complete (because their use is generally not recommended). The platform client library and older auth libraries are required for the **API key** version of the sample app because API keys are unsupported by the Python [Translation API (product) client libraries](https://cloud.google.com/translate/docs/setup#installing_client_libraries) even though they _are_ [supported by the Python Natural Language API (product) client library](https://cloud.google.com/docs/authentication/api-keys#using-with-client-libs). (**NOTE**: API key support in the Node.js (product or platform) client libraries is unknown -- if anyone has a working example, please file an issue and submit a PR.)

This code sample is only for (typically) non-GCP users who want to experiment with the APIs without the complexities of ADC, service accounts or OAuth client IDs. To run the API key sample, create an API key in the DevConsole and assign it to a variable named `API_KEY` in a `settings.py` file accessible to the script. More information including detailed steps are available in the [blog post](https://dev.to/wescpy/text-based-language-processing-enhanced-with-aiml-1b1h).

When compared to the standard version, _product_ client libraries and ADC vs. _platform_ client library and API key, you'll note there many similarities:

<img width="1639" alt="transnatlang-diffs" src="https://github.com/wescpy/google/assets/1102504/0ae03ec6-afb0-4fbc-b644-c3e12c41a548">
