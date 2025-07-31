# "Gmail 'chatty' threads" code samples

## Introduction
This repo contains developer code samples from the _upcoming post_ on the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy) demonstrating how to use the Gmail API to look for "chatty" threads, that is, threads that have at least 3 messages (one original post ["OP"] and a pair of replies). It's a more useful "Hello World!" for getting started with the [Gmail API](https://developers.google.com/gmail); if you have an extra Gmail account specifically for mailing lists, the code may actually be useful. This type of Gmail API functionality is also an example that can be implemented as part of an MCP (model context protocol) server for use with agentic apps.

<!--![Gmail banner from post?]()-->


## Code samples
The sample apps from the post come in several versions. This table helps you pick one that matches your needs best. Complete the setup & prerequisites below to ensure the samples will run if you haven't already.

Sample | Description | Tech info
--- | --- | ---
**Python** _(current auth libs)_ ||
[`python/gmail_chatty_threads.py`](python/gmail_chatty_threads.py) | Gmail 'chatty' threads sample | Python 2 & 3 combo version using current auth libs (`google.auth`)
[`python/gmail_chatty_threads-3async.py`](python/gmail_chatty_threads-3async.py) | Gmail 'chatty' threads sample | Modern Python 3-only (async, annotated) version using current auth libs (`google.auth`)
[`python/requirements.txt`](python/requirements.txt) | 3rd-party packages requirements | Current auth libs
**Python** _(old auth libs)_ ||
[`python/gmail_chatty_threads-old.py`](python/gmail_chatty_threads-old.py) | Gmail 'chatty' threads sample | Python 2 & 3 combo version using old auth libs (`oauth2client`)
[`python/requirements-old.txt`](python/requirements-old.txt) | 3rd-party packages requirements | Old auth libs
||
**Node.js**||
[`nodejs/gmail_chatty_threads.mjs`](nodejs/gmail_chatty_threads.mjs) | Gmail 'chatty' threads sample | ECMAScript module
[`nodejs/gmail_chatty_threads.js`](nodejs/gmail_chatty_threads.js) | Gmail 'chatty' threads sample | CommonJS script
[`nodejs/package.json`](nodejs/package.json) | 3rd-party packages requirements | _n/a_

| :memo: Python 2 and 3 supported |
|:---------------------------|
| Most of the world is on Python 3 today, but there are still some with dependencies on 2.x that make migration challenging. This is why there's a combo Python 2-3 compatible sample without newer features like `async/await`, type annotations, `f`-strings, etc. There's also a Python 3-only sample with those features for those desiring a more modern version. |


## Prerequisites/required setup
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
    - **NodeJS (16+)**:  Install required packages with this command:
        - `npm i`
    - **Python 2 or 3 (_new auth_):** In your normal or `virtualenv` environment, run the following command if using the current/new Python auth libraries (most everyone):
        - `pip install -Ur requirements.txt` (or `pip3`)
    - **Python 2 or 3 (_old auth_):** If you have dependencies on the older Python auth libraries and/or still have old code lying around that do (see warning sidebar below), run this command to ensure you have the latest/last versions of these libraries:
        - `pip install -Ur requirements-old.txt` (or `pip3`)
    - For Python specifically, 2.x means 2.7, and if you're already planning the migration to 3.x, you should **definitely** not be using _anything_ older than 2.6 (as it's the 1st release with 3.x-compatible features). For 3.x, it should work for nearly all releases, but 3.7 or newer are recommended.

| :boom: Caveat: `oauth2client` deprecated |
|:---------------------------|
| The older Python auth libraries, primarily `oauth2client`, were [deprecated in 2017](https://github.com/googleapis/oauth2client/pull/714) in favor of modern replacements. However the newer libraries [do not support](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html#replacement) OAuth token storage, hence why the older `*-old.py` samples are generally always shorter than their modern equivalents. For now, `oauth2client` still works, even in maintenance mode, and provides automated, threadsafe, and 2.x/3.x-compatible storage of and access to OAuth2 tokens for users whereas the newer libraries do not (yet). See [this post](https://dev.to/googleworkspace/oauth-client-ids-dirty-little-secrets-old-new-python-auth-libraries-4mb7) to learn more about this change and the "diffs" between using them. |

| :memo: Old service account version in Gmail API documentation |
|:---------------------------|
| The Python code samples in this repo and corresponding blog post represent modern and more fully-featured versions of the original sample I created as a Googler years ago as [part of the Gmail API documentation](https://developers.google.com/workspace/gmail/api/guides/threads). Note that the version in the docs uses [service account auth](https://dev.to/wescpy/getting-started-with-google-apis-service-accounts-part-1-2fi0) rather than OAuth client ID (user) auth, standard for requesting end-user permission. Service accounts are useful for Google Workspace ("GWS") domain administrators who perform tasks for multiple users of GWS domains without requesting individual permission from users to access the Gmail API on their behalf; this is known as [domain-wide delegation](https://support.google.com/a/answer/162106) or "DWD". |
