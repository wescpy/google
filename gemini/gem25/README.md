# Google Gemini 2.5 API samples

## Old (separate) client libraries and current (combined) client library

These are the code samples from the _upcoming 6th post_ in the [Gemini API series](https://dev.to/wescpy/series/27183) for running on the [Google AI](https://ai.google.dev) (GAI) platform or the [Vertex AI](https://cloud.google.com/vertex-ai) (GCP) platform. More information about the scripts are in the post.

| :exclamation: Platform requirements |
|:---------------------------|
| **GAI**: [API key](https://cloud.google.com/docs/authentication/api-keys-use) is required. Follow the instructions below. The GAI scripts will ***not*** run without an API key which should be either assigned to the `GEMINI_API_KEY` environment variable or saved to a local file, `.env` (Node.js) or `settings.py` (Python). |
| **GCP**: API key (as above) or better yet, [user auth via ADC](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) for local dev environments running these sample scripts. (For production, use [service accounts](https://cloud.google.com/docs/authentication#service-accounts).)


## Code samples
App | Platform(s) | Client library | Description
--- | --- | --- | ---
**Node.js**
[`gem25txt-simple-gai-cur.js`](/gemini/gem25/gem25txt-simple-gai-cur.js) | GAI | GenAI (current) | CommonJS Node.js script
[`gem25txt-simple-gai-cur.mjs`](/gemini/gem25/gem25txt-simple-gai-cur.mjs) | GAI | GenAI (current) | ECMAscript Node.js module
[`gem25txt-simple-gai-old.js`](/gemini/gem25/gem25txt-simple-gai-old.js) | GAI | GenerativeAI (old) | CommonJS Node.js script
[`gem25txt-simple-gai-old.mjs`](/gemini/gem25/gem25txt-simple-gai-old.mjs) | GAI | GenerativeAI (old) | ECMAscript Node.js module
[`gem25txt-simple-gcp-cur.js`](/gemini/gem25/gem25txt-simple-gcp-cur.js) | GCP | GenAI (current) | CommonJS Node.js script
[`gem25txt-simple-gcp-cur.mjs`](/gemini/gem25/gem25txt-simple-gcp-cur.mjs) | GCP | GenAI (current) | ECMAscript Node.js module
[`gem25txt-simple-gcp-old.js`](/gemini/gem25/gem25txt-simple-gcp-old.js) | GCP | GenerativeAI (old) | CommonJS Node.js script
[`gem25txt-simple-gcp-old.mjs`](/gemini/gem25/gem25txt-simple-gcp-old.mjs) | GCP | GenerativeAI (old) | ECMAscript Node.js module
[`package.json`](/gemini/gem25/package.json) | _both platforms_ | _both libraries_ | NPM packages file
[`.env_TMPL`](/gemini/gem25/.env_TMPL) | _both platforms_ | _both libraries_ | `.env` template file
 | | |
**Python**
[`gem25txt-simple-gai-cur.py`](/gemini/gem25/gem25txt-simple-gai-cur.py) | GAI | GenAI (current) | Python 3 script
[`gem25txt-simple-gai-old.py`](/gemini/gem25/gem25txt-simple-gai-old.py) | GAI | VertexAI (old) | Python 3 script
[`gem25txt-simple-gcp-cur.py`](/gemini/gem25/gem25txt-simple-gcp-cur.py) | GCP | GenAI (current) | Python 3 script
[`gem25txt-simple-gcp-old.py`](/gemini/gem25/gem25txt-simple-gcp-old.py) | GCP | VertexAI (old) | Python 3 script
[`requirements.txt`](/gemini/gem25/requirements.txt) | _both platforms_ | _both libraries_ | `pip` requirements file
[`settings_TMPL.py`](/gemini/gem25/settings_TMPL.py) | _both platforms_ | _both libraries_ | `settings.py` template file


## General instructions (GAI & GCP)

### Node.js
1. Ensure your Node (and NPM) installation is up-to-date (recommend 18+)
1. Install all packages (old & new client libraries): `npm i`

### Python
1. Ensure your Python (and `pip`) installation is up-to-date (recommend 3.9+)
1. (optional) [Create & activate a virtual environment ("virtualenv") for isolation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)
    - `python3 -m venv .myenv; source .myenv/bin/activate`
    - For the commands below, depending on your system configuration, you will use one of (`pip`, `pip3`, `python3 -m pip`), but the instructions are generalized to `pip`.
1. (optional) Update `pip` and install `uv`: `pip install -U pip uv`
1. Install all packages (old & new client libraries): `uv pip install -Ur requirements.txt` (drop `uv` if you didn't install it)


## GAI-specific instructions

### Node.js
1. [Create API key](https://makersuite.google.com/app/apikey) and either save to `GEMINI_API_KEY` environment variable or copy the `.env_TMPL` file to `.env` and assign the key to `API_KEY`.
1. Run any of the Node scripts, e.g., `node gem25txt-simple-gai-old.mjs`

### Python
1. [Create API key](https://makersuite.google.com/app/apikey) and either save to `GEMINI_API_KEY` environment variable or copy the `settings_TMPL.py` file to `settings.py` and assign the key to `API_KEY`.
1. Run any of the Python scripts, e.g., `python gem25txt-simple-gai-cur.py` (or `python3`)


## GCP-specific instructions

### Node.js
1. Create credentials (choose one):
    - (_recommended_) [Login with user auth & set ADC for local dev environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    - API key: follow same instructions as for GAI above
1. Run any of the Node scripts, e.g., `node gem25txt-simple-gcp-cur.js`

### Python
1. Create credentials (choose one):
    - (_recommended_) [Login with user auth & set ADC for local dev environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    - API key: follow same instructions as for GAI above
1. Run any of the Python scripts, e.g., `python gem25txt-simple-gcp-old.py` (or `python3`)
