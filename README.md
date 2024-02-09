# Google developer code samples

## Introduction

This repo contains developer code samples from the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy) as well as older but still relevant content such as posts from [the old G Suite blog](https://gsuite-developers.googleblog.com/2015/) as well as [my old Python and Google API blog](https://wescpy.blogspot.com/).


## Content structure

Samples demonstrating only one product group are prefixed under the product group name (see table below) while cross-product samples will go into `multi`.

Directory | API families
--- | ---
`apps` | [Google Workspace](http://developers.google.com/gsuite) ("GWS"; formerly G Suite and Google Apps)
`cloud` | [Google Cloud](http://cloud.google.com) (Platform; "GCP")
`maps` | [Google Maps](http://developers.google.com/maps) (Platform; "GMP")
`youtube` | [YouTube](http://developers.google.com/youtube)
`multi` | (multi-product sample apps) [_N/A at this time_]

<figcaption>Code sample categories</figcaption>


### Initial samples

The chart below identifies the current samples available:

App | Sample | Blog post
--- | --- | ---
[`apps/sheets_display.py`](/apps/sheets_display.py) | Display contents of public Sheet | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`apps/drive_list.py`](http://github.com/wescpy/gsuite-apis-intro/python/drive_list.py) (other repo) | Display first 100 files/folders in Google Drive (Python old auth) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
[`apps/drive_list-new.py`](http://github.com/wescpy/gsuite-apis-intro/python/drive_list-new.py) (other repo) | Display first 100 files/folders in Google Drive (Python new auth) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
[`apps/drive_list.js`](http://github.com/wescpy/gsuite-apis-intro/blob/master/nodejs/drive_list.js) (other repo) | Display first 100 files/folders in Google Drive (Node.js Standard JS [`require`]) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
[`apps/drive_list.mjs`](http://github.com/wescpy/gsuite-apis-intro/blob/master/nodejs/drive_list.mjs) (other repo) | Display first 100 files/folders in Google Drive (Node.js ES Module JS [`import`]) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
[`cloud/language/nlp_sent_query.py`](/cloud/language/nlp_sent_query.py) | Sentiment analysis of text using Natural Language API w/lower-level _platform_ Google APIs client library | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`cloud/language/nlp_sent_query-gcp.py`](/cloud/language/nlp_sent_query-gcp.py) | Sentiment analysis of text using Natural Language API w/higher-level _product_ GCP client library | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`cloud/appengine/nodejs`](/cloud/appengine/nodejs) | Node.js App Engine "Hello World!" sample app | [Exploring GAE]()
[`cloud/appengine/python3`](/cloud/appengine/python3) | Python 3 App Engine "Hello World!" sample app | [Exploring GAE]()
[`maps/maps_loc_query.py`](/maps/maps_loc_query.py) | Geolocate (public) address with Maps Geocoding API | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`youtube/yt_video_query.py`](/youtube/yt_video_query.py) | Query for (public) YouTube videos (Python) | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`youtube/yt_video_query.js`](/youtube/yt_video_query.js) | Query for (public) YouTube videos (Node.js) | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)

<figcaption>Code sample table of contents</figcaption>


## Support

I will provide "support" in a "best-effort" manner. I am open to fixes and updates to existing samples and will carry over relevant changes to affected blog posts. File a "bug" against an existing sample with details. If there is a "missing" sample you are proposing that doesn't exist, also file a bug and state why it would benefit the community. Currently, only Python and JavaScript (Node.js, Apps Script) samples are being considered.
