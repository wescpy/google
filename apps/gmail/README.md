# "Gmail 'chatty' threads" code samples

## Introduction
This repo contains developer code samples from [this Gmail API post](https://bit.ly/4ljSH2W) on the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy) demonstrating how to use the Gmail API to look for "chatty" threads, that is, threads that have at least 3 messages (one original post ["OP"] and a pair of replies). It's a more useful "Hello World!" for getting started with the [Gmail API](https://developers.google.com/gmail); if you have an extra Gmail account specifically for mailing lists, the code may actually be useful. This type of Gmail API functionality is also an example that can be implemented as part of an MCP (model context protocol) server for use with agentic apps.

[![Gmail banner](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7f8mmfnxcxtozklil0dj.png)](https://bit.ly/4ljSH2W)


## Code samples
The sample apps from the post come in several versions. This table helps you pick one that matches your needs best. Complete the setup & prerequisites below to ensure the samples will run if you haven't already.

Sample | Description
--- | ---
**Python** _(current auth libs)_ |
[`gmail_chatty_threads.py`](python/gmail_chatty_threads.py) | Python 2 & 3 combo version using current auth libs (`google.auth`)
[`gmail_chatty_threads-3async.py`](python/gmail_chatty_threads-3async.py) | Modern Python 3-only (async, annotated) version using current auth libs (`google.auth`)
[`requirements.txt`](python/requirements.txt) | 3rd-party packages requirements with current auth libs
**Python** _(old auth libs)_ |
[`gmail_chatty_threads-old.py`](python/gmail_chatty_threads-old.py) | Python 2 & 3 combo version using old auth libs (`oauth2client`)
[`requirements-old.txt`](python/requirements-old.txt) | 3rd-party packages requirements with old auth libs
||
**Node.js**|
[`gmail_chatty_threads.mjs`](nodejs/gmail_chatty_threads.mjs) | ECMAScript module
[`gmail_chatty_threads.js`](nodejs/gmail_chatty_threads.js) | CommonJS script
[`package.json`](nodejs/package.json) | 3rd-party packages requirements

| :memo: **Python 2 and 3 supported** |
|:---------------------------|
| Most of the world is on Python 3 today, but there are still some with dependencies on 2.x that make migration challenging. This is why I aim to create Python 2-3 compatible samples, to help those continuing to migrate. There's also a modern Python 3-only sample with newer features like `async/await`, type annotations, `f`-strings, etc. for those who don't care about 2.x support. |


## Prerequisites/required setup
1. ***System requirements***
    - For Python 2 specifically, that means 2.7 only.
    - For Python 3, I strongly suggest 3.9 or newer.
    - For Node.js, I suggest 16 or newer.
1. ***Create a new project*** [from the Cloud/developer console](https://console.cloud.google.com/projectcreate) or with `gcloud projects create . . .`; or reuse an existing project
1. ***Enable the Gmail API***. Pick your preferred method of these three common ways to enable APIs:
    - **DevConsole manually** -- Enable the API manually from the DevConsole by following these steps:
        1. Go to [DevConsole](http://console.developers.google.com)
        1. Click on **Library** tab in the left-nav; search for "Gmail", and enable
    - **DevConsole link** -- You may be new to Google APIs or don't have experience enabling APIs manually in the DevConsole. If this is you...
        1. Check out the [API listing page](https://console.cloud.google.com/apis/library/gmail.googleapis.com) to learn more about the API and enable it from there.
        1. Alternatively, skip the API info and click [this link](http://console.developers.google.com/start/api?id=gmail) for the enable button.
    - **Command-line** (`gcloud`) -- Those who prefer working in a terminal can enable APIs with a single command in the [Cloud Shell](https://cloud.google.com/shell) or locally on your computer if you [installed the Cloud SDK](https://cloud.google.com/sdk/install) which includes the `gcloud` command-line tool (CLI) and initialized its use.
        1. If this is you, issue this command to enable the API: `gcloud services enable gmail.googleapis.com`
        1. Confirm all the APIs you've enabled with this command: `gcloud services list`
1. ***Create OAuth client ID & secret [credentials](https://console.cloud.google.com/apis/credentials)*** and save the file to your local filesystem as `client_secret.json`. The code samples **will not run** without this file present.
1. ***Install the Google APIs client library***:
    - **Node**:  Install required packages with:
        - `npm i`
    - **Python 2 or 3 (_new auth_):** In your normal or `virtualenv` environment, install the current/new Python auth libraries (most everyone) with one of these:
        - `pip install -Ur requirements.txt` (or `pip3`)
        - `uv pip install -Ur requirements.txt` (if you use `uv`)
        - Manually install packages by name (see `requirements.txt`)
    - **Python 2 or 3 (_old auth_):** If you have dependencies on the older Python auth libraries and/or still have old code lying around that do (see warning sidebar below), run one of these options instead:
        - `pip install -Ur requirements-old.txt` (or `pip3`)
        - `uv pip install -Ur requirements-old.txt` (if you use `uv`)
        - Manually install packages by name (see `requirements-old.txt`)

| :boom: Caveat: `oauth2client` deprecated |
|:---------------------------|
| The older Python auth library, `oauth2client`, was [deprecated in 2017](https://github.com/googleapis/oauth2client/pull/714). However the current library [does not support](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html#replacement) OAuth token storage, hence why `*-old.py` samples like the above are shorter than their modern equivalents. For now, `oauth2client` still works, even in maintenance mode, and provides threadsafe and 2.x/3.x-compatible storage of and access to OAuth2 tokens. [This post](https://dev.to/googleworkspace/oauth-client-ids-dirty-little-secrets-old-new-python-auth-libraries-4mb7) sheds more light on this change. Google won't provide migration guides showing "before & after," so their "dirty little secret" is one of the reasons why I'm here. It helps both developers and vibecoding LLMs understand this transition so all can produce modern code or migrate/fix old library code. |

| :memo: Service account alternative in API docs |
|:---------------------------|
| Around the time of the original post & video, I created an alternative Python version of the app using [service account auth](https://dev.to/wescpy/getting-started-with-google-apis-service-accounts-part-1-2fi0) which was added to the [Threads page](https://developers.google.com/workspace/gmail/api/guides/threads) of the documentation. While OAuth client IDs are standard for user permission, service accounts are useful for Workspace administrators performing tasks for multiple GWS domain users without needing to request individual user permission to perform actions on their behalf; this is known as [domain-wide delegation](https://support.google.com/a/answer/162106) ("DWD"). I'll cover the differences and conversion between user & service account auth in a future post. For now, that alternative sample in the docs (ported to the current auth library) suffices. Impatient? Check [this post](http://goo.gle/3nPxmlc) and [code repo](https://github.com/wescpy/analyze_gsimg) which has samples in all 4 combinations (and more): old auth vs. new auth and OAuth client IDs vs. service accounts credentials. |
