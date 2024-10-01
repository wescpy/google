# "Uploading CSV files to Google Drive and importing them as Google Sheets" code samples

## Introduction
This repo contains developer code samples from an _upcoming_ post covering how to upload CSV files to Google Drive as-is as well as how to do the same but import them into Google Sheets format featured on the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy). The samples are available in Python and Node.js/JavaScript.

| :memo: Python 2 and 3 supported |
|:---------------------------|
| Most of the world is on Python 3 today, but there are still some with dependencies on 2.x that make migration challenging. The Python code samples in this repo are both Python 2-3 compatible, hence why you don't see newer features like `async-await`, type annotations, `f`-strings, etc. |


## Code samples

The sample app from the post come in several versions. This table will help you choose which works for you. Be sure to complete the setup & prerequisites below to ensure the samples will run if you haven't already.

Sample | Description | Runtime or technology
--- | --- | ---
[`python/drive_csv_upload.py`](python/drive_csv_upload.py) | Upload CSV as-is to Drive | Python (2 & 3) version using current auth libs (`google.auth`)
[`python/drive_csv_import.py`](python/drive_csv_import.py) | Import CSV to Drive as Sheets | Python (2 & 3) version using current auth libs (`google.auth`)
[`python/drive_csv_upload-old.py`](python/drive_csv_upload-old.py) | Upload CSV as-is to Drive | Python (2 & 3) version using old auth libs (`oauth2client`)
[`python/drive_csv_import-old.py`](python/drive_csv_import-old.py) | Import CSV to Drive as Sheets | Python (2 & 3) version using old auth libs (`oauth2client`)
[`python/inventory.csv`](python/inventory.csv) | Sample inventory file | CSV (same as Node.js version)
||
[`nodejs/drive_csv_upload.js`](nodejs/drive_csv_upload.js) | Upload CSV as-is to Drive | CommonJS Node.js/JavaScript version
[`nodejs/drive_csv_upload.mjs`](nodejs/drive_csv_upload.mjs) | Upload CSV as-is to Drive | Modern JavaScript/ECMAScript module
[`nodejs/drive_csv_import.js`](nodejs/drive_csv_import.js) | Import CSV to Drive as Sheets | CommonJS Node.js/JavaScript version
[`nodejs/drive_csv_import.mjs`](nodejs/drive_csv_import.mjs) | Import CSV to Drive as Sheets | Modern JavaScript/ECMAScript module
[`nodejs/inventory.csv`](nodejs/inventory.csv) | Sample inventory file | CSV (same as Python version)


## Prerequisites/required setup
1. ***Create a new project*** [from the Cloud/developer console](https://console.cloud.google.com/projectcreate) or with `gcloud projects create . . .`; or reuse an existing project
1. ***Enable the Google Drive API***. Pick your preferred method of these three common ways to enable APIs:
    - **DevConsole manually** -- Enable the API manually from the DevConsole by following these steps:
        - Go to [DevConsole](http://console.developers.google.com)
        - Click on **Library** tab in the left-nav; search for "Drive", and enable
    - **DevConsole link** -- You may be new to Google APIs or don't have experience enabling APIs manually in the DevConsole. If this is you...
        - Check out the [API listing page](https://console.cloud.google.com/apis/library/drive.googleapis.com) to learn more about the API and enable it from there.
        - Alternatively, skip the API info and click [this link](http://console.developers.google.com/start/api?id=drive) for the enable button.
    - **Command-line** (`gcloud`) -- Those who prefer working in a terminal can enable APIs with a single command in the [Cloud Shell](https://cloud.google.com/shell) or locally on your computer if you [installed the Cloud SDK](https://cloud.google.com/sdk/install) which includes the `gcloud` command-line tool (CLI) and initialized its use.
        - If this is you, issue this command to enable the API: `gcloud services enable drive.googleapis.com`
        - Confirm all the APIs you've enabled with this command: `gcloud services list`
1. ***Create OAuth client ID & secret [credentials](https://console.cloud.google.com/apis/credentials)*** and save the file to your local filesystem as `client_secret.json`. The code samples **will not run** without this file present.
1. ***Install the Google APIs client library***:
    - **NodeJS (16+)**:  Create a basic `package.json` and install required pkgs with this command:
        - `npm i googleapis @google-cloud/local-auth`
    - **Python 2 or 3 (_new auth_):** In your normal or `virtualenv` environment, run the following command if using the current/new Python auth libraries (most everyone):
        - `pip install -U google-api-python-client google-auth-httplib2 google-auth-oauthlib` (or `pip3`)
    - **Python 2 or 3 (_old auth_):** If you have dependencies on the older Python auth libraries and/or still have old code lying around that do (see warning sidebar below), run this command to ensure you have the latest/last versions of these libraries:
        - `pip install -U pip google-api-python-client oauth2client` (or `pip3`)
    - For Python specifically, 2.x means 2.7, and if you're already planning the migration to 3.x, you should **definitely** not be using _anything_ older than 2.6 (as it's the 1st release with 3.x-compatible features). For 3.x, it should work for nearly all releases, but 3.7 or newer are recommend.

| :boom: Caveat: `oauth2client` deprecated |
|:---------------------------|
| The older Python auth libraries, primarily `oauth2client`, were [deprecated in 2017](https://github.com/googleapis/oauth2client/pull/714) in favor of modern replacements. However the newer libraries [do not support](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html#replacement) OAuth token storage, hence why the older `*-old.py` samples are generally always shorter than their modern equivalents. For now, `oauth2client` still works, even in maintenance mode, and provides automated, threadsafe, and 2.x/3.x-compatible storage of and access to OAuth2 tokens for users whereas the newer libraries do not (yet). |
