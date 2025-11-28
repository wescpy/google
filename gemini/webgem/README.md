# Google Gemini API web app samples

These are the code samples that are found in the [3rd post](https://dev.to/wescpy/gemini-api-102a-putting-together-a-basic-genai-web-app-3e3) in the [Gemini API series](https://dev.to/wescpy/series/27183).

| :exclamation: API key required |
|:---------------------------|
| An API key is required to use Google's Gemini API. Follow the instructions below. The app will ***not*** run without a `.env` file (Node.js) or `settings.py` (Python). (You can alternatively refactor the Python version to use `.env`, similar to Node, but would have to integrate use of `python-dotenv`.) Templates for `.env` and `settings.py` are provided in the repo. |

| :bulb: Deploy this app to GCP serverless platforms |
|:---------------------------|
| There is an alternative version to this app that allow it to be deployed to GCP serverless platforms like Cloud Run and App Engine. It is nearly-identical to the app in this repo except it contains additional configuration files making it deployable to the cloud. If you're looking for the cloud-capable version, you can find it in [this repo](https://github.com/wescpy/nebulous-serverless/tree/main/multi/webgem)... a separate post covering it is in the works. |


## Code samples
App | Description | Platform
--- | --- | ---
[`nodejs/.env_TMPL`](/gemini/webgem/nodejs/.env_TMPL) | `.env` template | Node.js (all)
[`nodejs/package.json`](/gemini/webgem/nodejs/package.json) | 3rd-party packages | Node.js (all)
[`nodejs/main.js`](/gemini/webgem/nodejs/main.js) | Express.js sample app | Node.js (CommonJS)
[`nodejs/main.mjs`](/gemini/webgem/nodejs/main.mjs) | Express.js sample app | Node.js (modern JS/ECMAScript module)
[`nodejs/templates/index.html`](/gemini/webgem/nodejs/templates/index.html) | Web template | Nunjucks (identical to Jinja2)
 | |
[`python/settings_TMPL.py`](/gemini/webgem/python/settings_TMPL.py) | `settings.py` template | Python 3
[`python/requirements.txt`](/gemini/webgem/python/requirements.txt) | Flask 3rd-party packages | Python 3
[`python/main.py`](/gemini/webgem/python/main.py) | Flask sample app | Python 3
[`python/templates/index.html`](/gemini/webgem/python/templates/index.html) | Web template | Jinja2 (identical to Nunjucks)
 | |
[`python/fastapi/main.py`](/gemini/webgem/python/fastapi/main.py) | FastAPI sample app | Python 3
[`python/fastapi/requirements.txt`](/gemini/webgem/python/fastapi/requirements.txt) | FastAPI 3rd-party packages | Python 3


## Instructions

### Node.js

1. Ensure your Node (and NPM) installation is up-to-date (recommend 18+)
1. `cd nodejs`
1. Install packages: `npm i` (see `package.json` for package names)
1. [Create API key](https://makersuite.google.com/app/apikey) and set in `.env` file as `API_KEY = <YOUR_API_KEY>;`
1. Run `node main.js` or `node main.mjs`

### Python

1. Ensure your Python (and `pip`) installation is up-to-date (recommend 3.9+)
1. `cd python`
1. (optional) [Create & activate a virtual environment ("virtualenv") for isolation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)
    - `python3 -m venv .myenv; source .myenv/bin/activate`
    - For the commands below, depending on your system configuration, you will use one of (`pip`, `pip3`, `python3 -m pip`), but the instructions are generalized to `pip`.
1. (optional) Update `pip` and install `uv`: `pip install -U pip uv`
1. Install packages: `uv pip install -Ur requirements.txt` (drop `uv` if you didn't install it)
1. [Create API key](https://makersuite.google.com/app/apikey) and set in `settings.py` file as `API_KEY = <YOUR_API_KEY>`
1. Run `python main.py` (or `python3`)

| :memo: Gemini API also accessible from GCP Vertex AI |
|:---------------------------|
| While these sample apps access the Gemini API from Google AI, a great place for beginners and those experimenting with it, the API is also accessible from GCP's Vertex AI platform for those ready to use Gemini for production workloads. To learn more about calling the Gemini API from either (or both) places, see [this post](https://bit.ly/4kFkmLm). The `.env_TMPL` and `settings_TMPL.py` files have placeholders for the required GCP information to call the Gemini API from the Vertex AI platform. |
