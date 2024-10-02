# @wescpy Google blog code samples

## Introduction

This repo contains developer code samples from the [**Coding #Python and #Google with @wescpy** blog](https://dev.to/wescpy) as well as older but still relevant content such as posts from [the old G Suite blog](https://gsuite-developers.googleblog.com/2015/) as well as @wescpy's [former Google/Python blog](https://wescpy.blogspot.com). Where possible and time-permitting, equivalent Node.js samples will be available as well.


## Content structure

Samples demonstrating only one product group are prefixed under the product group name (see table below) while cross-product samples will go into `multi`.

Directory | API families
--- | ---
[`apps`](/apps) | [Google Workspace](https://developers.google.com/gsuite) ("GWS"; formerly G Suite and Google Apps)
[`cloud`](/cloud) | [Google Cloud](https://cloud.google.com) (Platform; "GCP")
[`gemini`](/gemini) | [Gemini API](https://ai.google.dev/docs/gemini_api_overview)
[`maps`](/maps) | [Google Maps](https://developers.google.com/maps) (Platform; "GMP")
[`youtube`](/youtube) | [YouTube](https://developers.google.com/youtube)
`multi` | (multi-product sample apps) [_N/A at this time_]
<figcaption><i>Code sample categories</i></figcaption>


### Code samples

The chart below identifies the code samples and posts covering them:

App | Sample | Blog post
--- | --- | ---
[`apps/export-doc-pdf/`](/apps/export-doc-pdf) | Export Google Docs as PDF (Node.js & Python) | [Export Google Docs as PDF](https://dev.to/googleworkspace/export-google-docs-as-pdf-without-the-docs-api-9o4)
[`apps/import-csv/`](/apps/import-csv) | Import CSV to Google Sheets (Node.js & Python) | [Import CSV to Google Sheets](https://dev.to/wescpy/import-csv-to-google-sheets-without-the-sheets-api-20g1)
[`apps/sheets_display.py`](/apps/sheets_display.py) | Display contents of public Sheet | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`apps/drive_list.py`](https://github.com/wescpy/gsuite-apis-intro/blob/master/python/drive_list.py) (other repo) | Display first 100 files/folders in Google Drive (Python old auth) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
[`apps/drive_list-new.py`](http://github.com/wescpy/gsuite-apis-intro/blob/master/python/drive_list-new.py) (other repo) | Display first 100 files/folders in Google Drive (Python new auth) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
[`apps/drive_list.js`](http://github.com/wescpy/gsuite-apis-intro/blob/master/nodejs/drive_list.js) (other repo) | Display first 100 files/folders in Google Drive (Node.js CommonJS [`require`]) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
[`apps/drive_list.mjs`](http://github.com/wescpy/gsuite-apis-intro/blob/master/nodejs/drive_list.mjs) (other repo) | Display first 100 files/folders in Google Drive (Node.js ES Module [`import`]) | [OAuth client ID 3](https://dev.to/wescpy/getting-started-using-google-apis-workspace-33-2me0)
&nbsp; | &nbsp; | &nbsp;
[`cloud/language/nlp_sent_query.py`](/cloud/language/nlp_sent_query.py) | Sentiment analysis of text using Natural Language API w/lower-level _platform_ Google APIs client library | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`cloud/language/nlp_sent_query-gcp.py`](/cloud/language/nlp_sent_query-gcp.py) | Sentiment analysis of text using Natural Language API w/higher-level _product_ GCP client library | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6)
[`cloud/appengine/nodejs`](/cloud/appengine/nodejs) | Node.js App Engine "Hello World!" | Exploring GAE (_TBD_)
[`cloud/appengine/python3`](/cloud/appengine/python3) | Python 3 App Engine "Hello World!" | Exploring GAE (_TBD_)
[`cloud/transnatlang/`](/cloud/transnatlang) | Text-based language processing (Node.js & Python) | [Text-based language processing](https://dev.to/wescpy/text-based-language-processing-enhanced-with-aiml-1b1h)
&nbsp; | &nbsp; | &nbsp;
[`gemini/gemtxt-simple-gai.py`](/gemini/gemtxt-simple-gai.py) | Google AI Gemini Pro 1.0 API Python sample | [Gemini API "Hello World!"](https://dev.to/wescpy/a-better-google-gemini-api-hello-world-sample-4ddm)
[`gemini/gemtxt-simple-gai.js`](/gemini/gemtxt-simple-gai.js) | Google AI Gemini Pro 1.0 API (CommonJS) Node.js sample | [Gemini API "Hello World!"](https://dev.to/wescpy/a-better-google-gemini-api-hello-world-sample-4ddm)
[`gemini/gemtxt-simple-gai.mjs`](/gemini/gemtxt-simple-gai.mjs) | Google AI Gemini Pro 1.0 API (modern JS/ECMAScript module) Node.js sample | [Gemini API "Hello World!"](https://dev.to/wescpy/a-better-google-gemini-api-hello-world-sample-4ddm)
[`gemini/gemtxt-simple-gcp.py`](/gemini/gemtxt-simple-gcp.py) | GCP Vertex AI Gemini Pro 1.0 API Python sample | [Gemini API "Hello World!"](https://dev.to/wescpy/a-better-google-gemini-api-hello-world-sample-4ddm)
[`gemini/gemtxt-simple10-gai.py`](/gemini/gemtxt-simple10-gai.py) | Google AI Gemini 1.0 Pro Latest | [Gemini 102: Beyond "Hello World!"](https://dev.to/wescpy/gemini-api-102-next-steps-beyond-hello-world-1pb7)
[`gemini/gemtxt-stream10-gai.py`](/gemini/gemtxt-stream10-gai.py) | Google AI Gemini 1.0 Pro Latest | [Gemini 102: Beyond "Hello World!"](https://dev.to/wescpy/gemini-api-102-next-steps-beyond-hello-world-1pb7)
[`gemini/gemtxt-simple10-chat-gai.py`](/gemini/gemtxt-simple10-chat-gai.py) | Google AI Gemini 1.0 Pro Latest | [Gemini 102: Beyond "Hello World!"](https://dev.to/wescpy/gemini-api-102-next-steps-beyond-hello-world-1pb7)
[`gemini/gemmmd-simple10loc-gai.py`](/gemini/gemmmd-simple10loc-gai.py) | Google AI Gemini 1.0 Pro Vision Latest | [Gemini 102: Beyond "Hello World!"](https://dev.to/wescpy/gemini-api-102-next-steps-beyond-hello-world-1pb7)
[`gemini/gemmmd-simple10url-gai.py`](/gemini/gemmmd-simple10url-gai.py) | Google AI Gemini 1.0 Pro Vision Latest | [Gemini 102: Beyond "Hello World!"](https://dev.to/wescpy/gemini-api-102-next-steps-beyond-hello-world-1pb7)
[`gemini/webgem/`](/gemini/webgem) | Google AI Gemini 1.5 Flash web apps (Node.js & Python) | [Gemini 102a: Creating basic gen AI web apps](https://dev.to/wescpy/gemini-api-102a-putting-together-a-basic-genai-web-app-3e3)
&nbsp; | &nbsp; | &nbsp;
[`maps/`](/maps) | Maps Geocoding, Directions, and Time Zone APIs (Node.js & Python) | [Explore the world with Maps APIs](https://dev.to/wescpy/explore-the-world-with-google-maps-apis-lhj)
[`maps/maps_geocode.py`](/maps/maps_geocode.py) | Geolocate address with Maps Geocoding API | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6) and [Explore the world with Maps APIs](https://dev.to/wescpy/explore-the-world-with-google-maps-apis-lhj)
&nbsp; | &nbsp; | &nbsp;
[`youtube/`](/youtube) | Query for (public) YouTube videos (Node.js & Python) | [Intro to the YouTube APIs](https://dev.to/wescpy/intro-to-the-youtube-apis-searching-for-videos-5a0o)
[`youtube/yt_video_query.py`](/youtube/yt_video_query.py) | Query for (public) YouTube videos (Python) | [API keys 2](https://dev.to/wescpy/getting-started-using-google-apis-api-keys-part-2-38i6) (and Intro to the YouTube APIs)
<figcaption><i>Code sample table of contents</i></figcaption>


## Support

"Support" will be provided in a "best-effort" manner. Open to fixes and updates to existing samples and affected blog posts. File a "bug" against an existing sample with details. If there is a "missing" sample you are proposing that doesn't exist (whether you write the code and submit the PR or are requesting someone do it), also file a bug and state why it would benefit the community. Currently, only (server-side) Python and JavaScript (Node.js, Apps Script) samples are being considered.
