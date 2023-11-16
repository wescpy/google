# Google developer code samples

## Introduction

This repo contains developer code samples from the [`Coding #Python and #Google with @wescpy` blog](https://dev.to/wescpy) as well as older but still relevant content such as posts from [the old G Suite blog](https://gsuite-developers.googleblog.com/2015/) as well as [my old Python and Google API blog](https://wescpy.blogspot.com/).


## Content structure

Samples demonstrating only one product group are prefixed under the product name, e.g., `cloud` == Google Cloud (Platform; GCP), `apps` == Google Workspace (GWS), etc., hierarchically followed by the specific product, e.g., `apps/drive`, `cloud/appengine`, etc., while cross-product samples will go into `multi` with product-based folder names, e.g., `apps-script-bigquery-sheets-slides`. Content and relevant APIs/platforms will be indexed in a table (coming soon) as they become available.

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

Name | Code | Sample | Blog post
--- | --- | --- | ---
`apps/sheets_display.py` | [link](/apps/sheets_display.py) | Display contents of public Sheet | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-4je6)
`apps/drive_list.py` (other repo) | [link](http://github.com/wescpy/gsuite-apis-intro/python/drive_list.py) | Display first 100 files/folders in Google Drive (Python old auth) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
`apps/drive_list-new.py` (other repo) | [link](http://github.com/wescpy/gsuite-apis-intro/python/drive_list-new.py) | Display first 100 files/folders in Google Drive (Python new auth) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
`apps/drive_list.js` (other repo) | [link](http://github.com/wescpy/gsuite-apis-intro/nodejs/drive_list.js) | Display first 100 files/folders in Google Drive (Node.js Standard JS [`require`]) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
`apps/drive_list.mjs` (other repo) | [link](http://github.com/wescpy/gsuite-apis-intro/nodejs/drive_list.mjs) | Display first 100 files/folders in Google Drive (Node.js ES Module JS [`import`]) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
`cloud/nlp_sent_query.py` | [link](/cloud/nlp_sent_query.py) | Sentiment analysis of text using Natural Language API w/lower-level _platform_ Google APIs client library | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-4je6)
`cloud/nlp_sent_query-gcp.py` | [link](/cloud/nlp_sent_query-gcp.py) | Sentiment analysis of text using Natural Language API w/higher-level _product_ GCP client library | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-4je6)
`maps/maps_loc_query.py` | [link](/maps/maps_loc_query.py) | Geolocate (public) address with Maps Geocoding API | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-4je6)
`youtube/yt_video_query.py` | [link](/youtube/yt_video_query.py) | Query for (public) YouTube videos (Python) | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-4je6)
`youtube/yt_video_query.js` | [link](/youtube/yt_video_query.js) | Query for (public) YouTube videos (Node.js) | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-4je6)

<figcaption>Code sample table of contents</figcaption>


## Contributions

I'm open to contributions from the community as well as updates and fixes to existing samples. I'll carry over relevant changes to affected blog posts. In either case, file a "bug" against an existing sample or that a sample you're proposing doesn't exist and why it would benefit the community. Currently, only Python and JavaScript (Node.js, Apps Script) samples are being considered.
