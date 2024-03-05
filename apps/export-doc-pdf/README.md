# "Exporting Google Docs documents as PDF" code samples

## Introduction
This repo contains developer code samples from a blog post covering how to export Google Docs documents as PDF (_coming soon_) featured on the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy). The samples are available in Python and Node.js/JavaScript.

| :memo: Python 2 and 3 supported |
|:---------------------------|
| Most of the world is on Python 3 today, but there are still some with dependencies on 2.x that make migration challenging. The Python code samples in this repo are both Python 2-3 compatible, hence why you don't see fancy features like `async-await` and `f`-strings. |


## Prerequisites/required setup
- **NodeJS** ***(16+):*** Create a basic `package.json` and install required pkgs with this command:
    - `npm init -y; npm i googleapis @google-cloud/local-auth`
- **Python 2 or 3** ***(_new auth_):*** In your normal or `virtualenv` environment, run the following command if using the current/new Python auth libraries (most everyone):
    - `pip install -U google-api-python-client google-auth-httplib2 google-auth-oauthlib` (or `pip3`)
- **Python 2 or 3** ***(_old auth_):*** If you have dependencies on the older Python auth libraries and/or still have old code lying around that do (see warning sidebar below), run this command to ensure you have the latest/last versions of these libraries:
    - `pip install -U pip google-api-python-client oauth2client` (or `pip3`)

| :boom: Caveat: `oauth2client` deprecated |
|:---------------------------|
| The older Python auth libraries, primarily `oauth2client`, were deprecated in 2017 in favor of modern replacements. However the newer libraries do not support OAuth token storage, hence why current code is slightly longer than any `*-old.py` samples. For now, `oauth2client` still works, even in maintenance mode, and provides automated, threadsafe, and 2.x/3.x-compatible storage of and access to OAuth2 tokens for users whereas the newer libraries do not (yet). |


## Code samples
App | Description
--- | ---
[`python/drive_export_doc_pdf.py`](python/drive_export_doc_pdf.py) | Python version usinusing new auth libs (`google.auth`)
[`python/drive_export_doc_pdf-old.py`](python/drive_export_doc_pdf-old.py) | Python version using old auth libs (`oauth2client`)
[`nodejs/drive_export_doc_pdf.js`](nodejs/drive_export_doc_pdf.js) | CommonJS Node.js/JavaScript version
[`nodejs/drive_export_doc_pdf.mjs`](nodejs/drive_export_doc_pdf.mjs) | Modern JavaScript/ECMAScript module
<figcaption><i>Featured code samples</i></figcaption>

