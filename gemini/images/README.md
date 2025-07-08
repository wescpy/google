# Google Gemini API image generation app samples

These are the code samples from the [5th post](https://dev.to/wescpy/generating-images-with-gemini-20-flash-from-google-448e) in the [Gemini API series](https://dev.to/wescpy/series/27183). More information about the scripts will be found there.

| :exclamation: API key required |
|:---------------------------|
| An API key is required to use the Gemini API. Follow the instructions below. The app will ***not*** run without being added to the `GEMINI_API_KEY` environment variable or saved to a local file, `.env` (Node.js) or `settings.py` (Python). |

## Code samples
App | Platform
--- | ---
[`gem20-image.js`](/gemini/images/gem20-image.js) | CommonJS Node.js script
[`gem20-image.mjs`](/gemini/images/gem20-image.mjs) | ECMAscript Node.js module
[`package.json`](/gemini/images/package.json) | NPM packages file
 | |
[`gem20-image.py`](/gemini/images/gem20-image.py) | Python 3 script
[`requirements.txt`](/gemini/images/requirements.txt) | `pip` requirements file

## Instructions

### Node.js

1. Ensure your Node (and NPM) installation is up-to-date (recommend 18+)
1. Install packages: `npm i`
1. [Create API key](https://makersuite.google.com/app/apikey) and either save to `.env` file as `GEMINI_API_KEY = <YOUR_API_KEY>;` or to `GEMINI_API_KEY` environment variable.
1. Run `node gem20-image.js` or `node gem20-image.mjs`

### Python

1. Ensure your Python (and `pip`) installation is up-to-date (recommend 3.9+)
1. (optional) [Create & activate a virtual environment ("virtualenv") for isolation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)
    - `python3 -m venv myenv; source myenv/bin/activate`
1. (optional) Update `pip` and install `uv`: `pip install -U pip uv`
1. Install packages:
    - `pip install -Ur requirements.txt` (or `pip3`)
    - (optional) If using `uv`: `uv pip install -Ur requirements.txt`
1. [Create API key](https://makersuite.google.com/app/apikey) and either save to `settings.py` file as `GEMINI_API_KEY = 'YOUR_API_KEY'` or to `GEMINI_API_KEY` environment variable.
1. Run `python gem20-image.py` (or `python3`)

| :memo: Gemini API also accessible from GCP Vertex AI |
|:---------------------------|
| While these sample scripts access the Gemini API from [Google AI](https://ai.google.dev), a great place for beginners and those experimenting with it, the API is also accessible from GCP's [Vertex AI platform](https://cloud.google.com/vertex-ai) for those ready to use Gemini in production workloads.
