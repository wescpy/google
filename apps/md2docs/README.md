# "Building a basic Markdown-to-Google Docs converter" code samples

## Introduction
This repo contains developer code samples from an upcoming [post on using the Google Docs API] covering that conversion to Sheets as well as uploading the CSV to Drive as-is. The post is posted as part of the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy). The samples are available in Python and Node.js/JavaScript.

![Markdown to Google Docs conversion](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7ha5q59y9q2aeu5hon9l.png)

![Stylization-Formatted string in Google Docs](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dk1lokm8xejpv386kpnu.png)


## Code samples

The sample apps from the post come in several versions. This table will help you choose which works for you. Be sure to complete the setup & prerequisites below to ensure the samples will run if you haven't already.

Sample | Description | Tech info
--- | --- | ---
[`python/md2docs.py`](python/md2docs.py) | Markdown-to-Google Docs converter | Python (2 & 3) version using current auth libs (`google.auth`)
[`python/md2docs-old.py`](python/md2docs-old.py) | Markdown-to-Google Docs converter | Python (2 & 3) version using old auth libs (`oauth2client`)
[`python/requirements.txt`](python/requirements.txt) | 3rd-party packages requirements | Current auth libs
[`python/requirements-old.txt`](python/requirements-old.txt) | 3rd-party packages requirements | Old auth libs
[`python/quickbrownfox.md`](python/quickbrownfox.md) | Data file | Markdown (same as Node.js version)
||
[`nodejs/md2docs.mjs`](nodejs/md2docs.mjs) | Markdown-to-Google Docs converter | Modern JavaScript/ECMAScript module
[`nodejs/md2docs.js`](nodejs/md2docs.js) | Markdown-to-Google Docs converter | CommonJS Node.js/JavaScript version
[`nodejs/package.json`](nodejs/package.json) | 3rd-party packages requirements | _n/a_
[`nodejs/quickbrownfox.md`](nodejs/quickbrownfox.md) | Data file | Markdown (same as Python version)

| :memo: Python 2 and 3 supported |
|:---------------------------|
| Most of the world is on Python 3 today, but there are still some with dependencies on 2.x that make migration challenging. The Python code samples in this repo are both Python 2-3 compatible, hence why you don't see newer features like `async/await`, type annotations, `f`-strings, etc. |


## Prerequisites/required setup
1. ***Create a new project*** [from the Cloud/developer console](https://console.cloud.google.com/projectcreate) or with `gcloud projects create . . .`; or reuse an existing project
1. ***Enable the Google Drive API***. Pick your preferred method of these three common ways to enable APIs:
    - **DevConsole manually** -- Enable the API manually from the DevConsole by following these steps:
        1. Go to [DevConsole](http://console.developers.google.com)
        1. Click on **Library** tab in the left-nav; search for "Drive", and enable
    - **DevConsole link** -- You may be new to Google APIs or don't have experience enabling APIs manually in the DevConsole. If this is you...
        1. Check out the [API listing page](https://console.cloud.google.com/apis/library/drive.googleapis.com) to learn more about the API and enable it from there.
        1. Alternatively, skip the API info and click [this link](http://console.developers.google.com/start/api?id=drive) for the enable button.
    - **Command-line** (`gcloud`) -- Those who prefer working in a terminal can enable APIs with a single command in the [Cloud Shell](https://cloud.google.com/shell) or locally on your computer if you [installed the Cloud SDK](https://cloud.google.com/sdk/install) which includes the `gcloud` command-line tool (CLI) and initialized its use.
        1. If this is you, issue this command to enable the API: `gcloud services enable drive.googleapis.com`
        1. Confirm all the APIs you've enabled with this command: `gcloud services list`
1. ***Create OAuth client ID & secret [credentials](https://console.cloud.google.com/apis/credentials)*** and save the file to your local filesystem as `client_secret.json`. The code samples **will not run** without this file present.
1. ***Install the Google APIs client library***:
    - **NodeJS (16+)**:  Install required packages with this command:
        - `npm i`
    - **Python 2 or 3 (_new auth_):** In your normal or `virtualenv` environment, run the following command if using the current/new Python auth libraries (most everyone):
        - `pip install -r requirements.txt` (or `pip3`)
    - **Python 2 or 3 (_old auth_):** If you have dependencies on the older Python auth libraries and/or still have old code lying around that do (see warning sidebar below), run this command to ensure you have the latest/last versions of these libraries:
        - `pip install -r requirements-old.txt` (or `pip3`)
    - For Python specifically, 2.x means 2.7, and if you're already planning the migration to 3.x, you should **definitely** not be using _anything_ older than 2.6 (as it's the 1st release with 3.x-compatible features). For 3.x, it should work for nearly all releases, but 3.7 or newer are recommended.

| :boom: Caveat: `oauth2client` deprecated |
|:---------------------------|
| The older Python auth libraries, primarily `oauth2client`, were [deprecated in 2017](https://github.com/googleapis/oauth2client/pull/714) in favor of modern replacements. However the newer libraries [do not support](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html#replacement) OAuth token storage, hence why the older `*-old.py` samples are generally always shorter than their modern equivalents. For now, `oauth2client` still works, even in maintenance mode, and provides automated, threadsafe, and 2.x/3.x-compatible storage of and access to OAuth2 tokens for users whereas the newer libraries do not (yet). |
