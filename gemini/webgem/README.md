# Google Gemini API web app samples

These are the code samples that are found in the [3rd post](https://dev.to/wescpy/gemini-api-102a-putting-together-a-basic-genai-web-app-3e3) in the [series introducing the Gemini API](https://dev.to/wescpy/series/27183).

| :exclamation: API key required |
|:---------------------------|
| An API key is required to use Google's Gemini API. Follow the instructions below. The app will ***not*** run without a `.env` file (Node.js) or `settings.py` (Python). |

## Code samples
App | Description | Platform
--- | --- | ---
[`webgem/nodejs/main.js`](/gemini/webgem/nodejs/main.js) | Express.js sample app | Node.js (CommonJS)
[`webgem/nodejs/main.mjs`](/gemini/webgem/nodejs/main.mjs) | Express.js sample app | Node.js (modern JS/ECMAScript module)
[`webgem/nodejs/templates/index.html`](/gemini/webgem/nodejs/templates/index.html) | Web template | Nunjucks (identical to Jinja2)
[`webgem/python/main.py`](/gemini/webgem/python/main.py) | Flask sample app | Python 3
[`webgem/python/templates/index.html`](/gemini/webgem/python/templates/index.html) | Web template | Jinja2 (identical to Nunjucks)

## Instructions

### Node.js

1. Ensure your Node (and NPM) installation is up-to-date (recommend 18+)
1. `cd nodejs`
1. Install packages: `npm i dotenv express multer nunjucks sharp @google/generative-ai`
1. [Create API key](https://makersuite.google.com/app/apikey) and set in `.env` file as `API_KEY = <YOUR_API_KEY>;`
1. Run `node main.js` or `node main.mjs`

### Python

1. Ensure your Python (and `pip`) installation is up-to-date (recommend 3.9+)
1. `cd python` and optionally [create & activate a virtual environment ("virtualenv") for isolation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)
1. Install packages: `pip install -U pip flask pillow google-generativeai` (or `pip3`)
1. [Create API key](https://makersuite.google.com/app/apikey) and set in `settings.py` file as `API_KEY = <YOUR_API_KEY>` ... you can alternatively put it into `.env` and use `python-dotenv`, similar to the Node version.
1. Run `python main.py` (or `python3`)

| :memo: Gemini API also accessible from GCP Vertex AI |
|:---------------------------|
| While these sample apps access the Gemini API from Google AI, a great place for beginners and those experimenting with it, the API is also accessible from GCP's Vertex AI platform for those ready to use Gemini for production workloads. To learn more about calling the Gemini API from either (or both) places, see my "A better Gemini API 'Hello World!' sample" post, the first in my [multi-part series on the Gemini API](https://dev.to/wescpy/series/27183).
