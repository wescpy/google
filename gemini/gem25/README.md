# Google Gemini 2.5 API samples

## Old (separate) client libraries and current (combined) client library

These are the code samples from the [6th post](https://bit.ly/4kFkmLm) in the [Gemini API series](https://dev.to/wescpy/series/27183) for running on the [Google AI](https://ai.google.dev) (GAI) and [Vertex AI](https://cloud.google.com/vertex-ai) (GCP) platforms. The post details how to use the Gemini 2.5 API as well as how to upgrade from older client libraries for Gemini 1.0 & 1.5. More information about migration and the code are in the post.

| :warning: Required credentials |
|:---------------------------|
| **GAI**: [API key](https://cloud.google.com/docs/authentication/api-keys-use) is required. Follow the instructions below. The GAI scripts will ***not*** run without an API key which should be either assigned to the `GEMINI_API_KEY` environment variable or saved to a local file, `.env` (Node.js) or `settings.py` (Python). |
| **GCP**: [User auth via ADC](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) for local dev environments is **required** to run the _old_ client library code and **recommended** for _current_ library code. The current library also supports API keys, but user auth/ADC is recommended as it's more secure. (For production, use [service accounts](https://cloud.google.com/docs/authentication#service-accounts). [I don't believe Google has documentation on how to do this, so I may have to do so in an upcoming post as I blog about things that Google should document.])

| :moneybag: Cost considerations |
|:---------------------------|
| **GAI**: Google AI has a free tier; see its [pricing page](https://ai.google.dev/pricing) for more information. |
| **GCP**: Vertex AI does ***not*** have a free tier, and an active billing account is required, so definitely check out its [pricing page](https://cloud.google.com/vertex-ai/generative-ai/pricing) to find out how much it'll cost to run the GCP scripts. |


## Code samples

### Script applications
Scripts are available in Python 3 & Node.js, the latter as both ECMAscript modules as well as CommonJS scripts. To compare like-scripts, the old client library version sits above its current client library equivalent.

Client library | Python | ECMAscript | CommonJS
--- | --- | --- | ---
**GAI**
GenerativeAI (old) | [`gem25txt-simple-gai-old.py`](/gemini/gem25/gem25txt-simple-gai-old.py) | [`gem25txt-simple-gai-old.mjs`](/gemini/gem25/gem25txt-simple-gai-old.mjs) | [`gem25txt-simple-gai-old.js`](/gemini/gem25/gem25txt-simple-gai-old.js)
GenAI (current) | [`gem25txt-simple-gai-cur.py`](/gemini/gem25/gem25txt-simple-gai-cur.py) | [`gem25txt-simple-gai-cur.js`](/gemini/gem25/gem25txt-simple-gai-cur.js) | [`gem25txt-simple-gai-cur.mjs`](/gemini/gem25/gem25txt-simple-gai-cur.mjs)
 | | | |
**GCP**
VertexAI (old) | [`gem25txt-simple-gcp-old.py`](/gemini/gem25/gem25txt-simple-gcp-old.py) | [`gem25txt-simple-gcp-old.mjs`](/gemini/gem25/gem25txt-simple-gcp-old.mjs) | [`gem25txt-simple-gcp-old.js`](/gemini/gem25/gem25txt-simple-gcp-old.js)
GenAI (current) | [`gem25txt-simple-gcp-cur.py`](/gemini/gem25/gem25txt-simple-gcp-cur.py) | [`gem25txt-simple-gcp-cur.mjs`](/gemini/gem25/gem25txt-simple-gcp-cur.mjs) | [`gem25txt-simple-gcp-cur.js`](/gemini/gem25/gem25txt-simple-gcp-cur.js)

### Configuration files
The config files include old & current client library packages and apply to both platforms.

Description | Python | Node.js
--- | --- | ---
Packages | [`requirements.txt`](/gemini/gem25/requirements.txt) | [`package.json`](/gemini/gem25/package.json)
Settings | [`settings_TMPL.py`](/gemini/gem25/settings_TMPL.py) | [`.env_TMPL`](/gemini/gem25/.env_TMPL)


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

1. **Set credentials:** [Create API key](https://makersuite.google.com/app/apikey) (or reuse existing one).
1. Either save the API key to `GEMINI_API_KEY` environment variable or copy the template for your language `.env_TMPL` (Node) or `settings_TMPL.py` (Python) file to `.env` (Node) or `settings.py` (Python) and assign the key to `API_KEY`.
    - If using the `GEMINI_API_KEY` environment variable, simplify the code to not look in `.env` or `settings.py` before running (use commented-out line). (This only affects scripts named `gem25txt-simple-gai-cur.*`.)
1. Run any of the scripts, e.g., `node gem25txt-simple-gai-old.mjs`, `python3 gem25txt-simple-gai-cur.py`, etc.

## GCP-specific instructions

1. **Set credentials:** [Login with user auth & set ADC for local dev environment](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    - The new client library supports API keys, so if you prefer this, then follow the GAI instructions above.
1. Copy the template for your language `.env_TMPL` (Node) or `settings_TMPL.py` (Python) file to `.env` (Node) or `settings.py` (Python) and set the values for `YOUR_GCP_PROJECT` and `YOUR_GCP_REGION`.
    - If using an API key instead of ADC, assign it to `API_KEY` in `.env` (Node) or `settings.py` (Python), and update the code to use it before running (use commented-out line). (This only affects scripts named `gem25txt-simple-gcp-cur.*`.)
1. Run any of the scripts, e.g., `node gem25txt-simple-gcp-cur.js`, `python3 gem25txt-simple-gcp-old.py`, etc.
