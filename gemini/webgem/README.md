# Google Gemini API web app samples

These are the code samples that are found in the [3rd post](https://dev.to/wescpy/gemini-api-102a-putting-together-a-basic-genai-web-app-3e3) in the [blog series introducing the Gemini API](https://dev.to/wescpy/series/27183).

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
1. `cd python`
1. Install packages: `pip install -U pip flask pillow google-generativeai` (or `pip3`)
1. [Create API key](https://makersuite.google.com/app/apikey) and set in `settings.py` file as `API_KEY = <YOUR_API_KEY>` ... you can alternatively put it into `.env` like the Node.js version and use `python-dotenv` like the Node version.
1. Run `python main.js` (or `python3`)