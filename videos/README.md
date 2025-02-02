# Google API/platform video library by @wescpy

I produced numerous developer videos during my time at Google from 2009-2023, primarily for Google Workspace (GWS) and Google Cloud (GCP) tools, APIs, and platforms. Whenever/whereever possible/available, you'll find relevant code samples and blog posts for each video.

Other product APIs featured in a video, or primary APIs featured but not discernable from the title or description are listed in the last column. All related code samples are in Python (2 and/or 3) unless otherwise indicated.

These are broken up by topic or product in order of the most content. Hold Ctrl/Command and mouseclick video thumbnails to open in another tab.


## Video and other "artifact" inventory


### Google APIs in general
Video | Title | Link(s) | Description | Relevant API(s), product(s), feature(s)
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/DYAwYxVs2TI/default.jpg)](https://youtu.be/DYAwYxVs2TI) | The Setup: Creating new apps using Google APIs | [post](https://developers.googleblog.com/2014/11/launchpad-online-for-developers-getting.html) | How to start using Google APIs | Cloud & Developers console
[![Watch video](https://i.ytimg.com/vi/h-gBeC9Y9cE/default.jpg)](https://youtu.be/h-gBeC9Y9cE) | Accessing Google APIs: Common code walkthrough | [post](https://developers.googleblog.com/2014/11/launchpad-online-for-developers-getting.html) | Understanding OAuth2 boilerplate basics (primarily for GWS APIs) | [Google APIs client libraries](https://developers.google.com/api-client-library) | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/T1FUDXRB7Ns/default.jpg)](https://youtu.be/T1FUDXRB7Ns) | Using field masks with Google APIs for partial response | [post](http://goo.gl/9kmAEf) | How to minimize data returned from Google API calls | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/W421BNZA_74/default.jpg)](https://youtu.be/W421BNZA_74) | Using field masks with update requests to Google APIs | [post](http://goo.gl/1Xhm04) | Choosing specific fields to update via Google API calls | _(tbd)_


### Google Workspace / GWS (Gmail, Google Drive, Docs, Sheets, Slides, etc.)

Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---

#### GWS general, platform, multiple API samples, etc.
Video | Title | Link(s) | Description | Relevant API(s), product(s), feature(s)
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/7uQ87m9RB74/default.jpg)](https://youtu.be/7uQ87m9RB74) | Creating great experiences with email markup | _(n/a)_ | What is ***email markup*** and how can it be useful? | Email markup
[![Watch video](https://i.ytimg.com/vi/NqumcYgj5LI/default.jpg)](https://youtu.be/NqumcYgj5LI) | Workspace (formerly G Suite) APIs: intro & overview | [post](http://t.co/XdKEWus0KI) | Basic intro to GWS APIs for student developers | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/kkp0aNGlynw/default.jpg)](https://youtu.be/kkp0aNGlynw) | Power Your Apps with Gmail, Google Drive, Calendar, Sheets, Slides, and More! | _(n/a)_ | Comprehensive GWS platform overview for developers, a Cloud Next '18 featured presentation | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/qBdG6cwnWps/default.jpg)](https://youtu.be/qBdG6cwnWps) | Transform the way you work with Google Chat bots/apps | _(n/a)_ | Launch presentation for Google Chat app/bot platform, a Google I/O 2018 featured presentation | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/h2_oiGv3ZdQ/default.jpg)](https://youtu.be/h2_oiGv3ZdQ) | Generating slides from spreadsheet data | [post](http://goo.gl/Yb06ZC) | Import spreadsheet data & charts into slide decks | Sheets & Slides APIs
[![Watch video](https://i.ytimg.com/vi/536IF8lJch4/default.jpg)](https://youtu.be/536IF8lJch4) | Performing Mail Merge with Google Docs | [post](http://goo.gle/2HZ8K6R) | Traditional "mail-merge" case study app (links to repo but no code in video) | Docs & Sheets APIs
[![Watch video](https://i.ytimg.com/vi/4KJostPGM8Q/default.jpg)](https://youtu.be/4KJostPGM8Q) | Extend Google Docs, Sheets, and Slides with Add-ons | _(n/a)_ | Creating add-ons for GWS, a Google Developers Day - India 2017 featured presentation | Apps Script, Docs, Sheets & Slides APIs
[![Watch video](https://i.ytimg.com/vi/2VpvWhDdXsI/default.jpg)](https://youtu.be/2VpvWhDdXsI) | Accessing Workspace (formerly G Suite) REST APIs | [post](http://goo.gle/3ateIIQ) | Accessing GWS REST APIs intro for Student Developers | _(tbd)_


#### Google Apps Script
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/vlvIa4DxiLw/default.jpg)](https://youtu.be/vlvIa4DxiLw) | Another Google (Apps) secret? | _(n/a)_ | Basic Apps Script intro
[![Watch video](https://i.ytimg.com/vi/xDovB0pu4OU/default.jpg)](https://youtu.be/xDovB0pu4OU) | Automate & extend with Google Apps Script | [post](http://goo.gle/2VF8xeC) | Basic Apps Script intro for student developers (modern version of above video)
[![Watch video](https://i.ytimg.com/vi/hkpj-xzXhaw/default.jpg)](https://youtu.be/hkpj-xzXhaw) | Accessing Google Maps from a spreadsheet?!? | _(n/a)_ | Access Google Maps from Google Sheets data | Google Maps Static API, Sheets API
[![Watch video](https://i.ytimg.com/vi/cKIVdzCf8ic/default.jpg)](https://youtu.be/cKIVdzCf8ic) | Automating YouTube stats with Google Apps Script | [post](http://goo.gl/nKfBQi) | Querying video information from data in spreadsheets | YouTube Data API, Sheets API
[![Watch video](https://i.ytimg.com/vi/rTDz-Zcn7yk/default.jpg)](https://youtu.be/rTDz-Zcn7yk) | Generating Google Slides from images | [post](http://goo.gl/sYL5AM) | Auto-generating slides in a deck based on a set of images | Slides API
[![Watch video](https://i.ytimg.com/vi/9cDvkVCcIWE/default.jpg)](https://youtu.be/9cDvkVCcIWE) | Expediting expense reports with Gmail add-ons | [post](http://goo.gl/KUVCDu), [codelab](http://g.co/codelabs/gmail-add-ons), [source](https://github.com/googleworkspace/gmail-add-on-codelab) | Using Gmail Add-ons to scan receipts in your inbox to expedite expense reporting | Gmail & Sheets APIs
[![Watch video](https://i.ytimg.com/vi/mKuINIBrR1g/default.jpg)](https://youtu.be/mKuINIBrR1g) | Making progress (bars) with Slides Add-ons | [post](http://goo.gl/69EJVw) | Adds a "progress bars" feature to Google Slides | Slides API
[![Watch video](https://i.ytimg.com/vi/L33hMxuoFtM/default.jpg)](https://youtu.be/L33hMxuoFtM) | Auto-generating Google Forms | [post](http://goo.gl/EK5edG) | How to automatically generate Google Forms | Forms API


#### Google Drive API
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/Z5G0luBohCg/default.jpg)](https://youtu.be/Z5G0luBohCg) | Listing your files in Google Drive | [post 1](https://developers.googleblog.com/2014/11/launchpad-online-for-developers-getting.html), [post 2](http://wescpy.blogspot.com/2014/11/authorized-google-api-access-from-python.html), [codelab](http://g.co/codelabs/gsuite-apis-intro), [source](https://github.com/wescpy/gsuite-apis-intro) | Basic GWS API script | Drive API
[![Watch video](https://i.ytimg.com/vi/-7YH6rdR-tk/default.jpg)](https://youtu.be/-7YH6rdR-tk) | Uploading & Downloading Files on Google Drive | [post](http://goo.gl/M3LQFQ) | Uploading & downloading files | Drive API
[![Watch video](https://i.ytimg.com/vi/5bifEBJRlaQ/default.jpg)](https://youtu.be/5bifEBJRlaQ) | Introducing Shared (formerly Team) Drives | [post](http://goo.gl/OWHzaN) | Coding ***Shared Drives*** | Drive API


#### Gmail API
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/L6hQCgxgzLI/default.jpg)](https://youtu.be/L6hQCgxgzLI) | Revolutionizing Email Access with Gmail | _(n/a)_ | Querying email headers in threads & messages | Gmail API
[![Watch video](https://i.ytimg.com/vi/kfeKF1zgwj0/default.jpg)](https://youtu.be/kfeKF1zgwj0) | Modifying email signatures in Gmail | [post](http://goo.gl/GbAOvb) | How to modify personal settings like email signatures | Gmail API
[![Watch video](https://i.ytimg.com/vi/9cDvkVCcIWE/default.jpg)](https://youtu.be/9cDvkVCcIWE) | Expediting expense reports with Gmail add-ons | [post](http://goo.gl/KUVCDu), [codelab](http://g.co/codelabs/gmail-add-ons), [source](https://github.com/googleworkspace/gmail-add-on-codelab) | Using Gmail Add-ons to scan receipts in your inbox to expedite expense reporting | Apps Script, Sheets API


#### Google Calendar API
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/tNo9IoZMelI/default.jpg)](https://youtu.be/tNo9IoZMelI) | Creating events in Google Calendar | [post](http://goo.gl/KuYMiq) | Creating calendar events | Calendar API
[![Watch video](https://i.ytimg.com/vi/Qd64idiKZWw/default.jpg)](https://youtu.be/Qd64idiKZWw) | Modifying events in Calendar | [post](http://goo.gl/J2XkXc) | Updating events in Google Calendar | Calendar API


#### Google Sheets API
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/VLdrgE8iJZI/default.jpg)](https://youtu.be/VLdrgE8iJZI) | Introducing the Google Sheets API v4 | [post](http://goo.gl/N1RPwC) | Create spreadsheet from rows of SQL data | Sheets API
[![Watch video](https://i.ytimg.com/vi/86q5TMzvRqo/default.jpg)](https://youtu.be/86q5TMzvRqo) | Formatting cells in Google Sheets | [post](http://goo.gl/U6Oljn) | Basic spreadsheet cell formatting | Sheets API
[![Watch video](https://i.ytimg.com/vi/T4pUOt4C36k/default.jpg)](https://youtu.be/T4pUOt4C36k) | Power and Flexibility of the "new" Google Sheets API | _(n/a)_ | Introduces the new v3 API features, a Google Developers Day - India 2017 featured presentation | Sheets API
[![Watch video](https://i.ytimg.com/vi/hkpj-xzXhaw/default.jpg)](https://youtu.be/hkpj-xzXhaw) | Accessing Google Maps from a spreadsheet?!? | _(n/a)_ | Access Google Maps from Google Sheets data | Google Maps Static API, Apps Script
[![Watch video](https://i.ytimg.com/vi/cKIVdzCf8ic/default.jpg)](https://youtu.be/cKIVdzCf8ic) | Automating YouTube stats with Google Apps Script | [post](http://goo.gl/nKfBQi) | Querying video information from data in spreadsheets | YouTube Data API, Apps Script
[![Watch video](https://i.ytimg.com/vi/9cDvkVCcIWE/default.jpg)](https://youtu.be/9cDvkVCcIWE) | Expediting expense reports with Gmail add-ons | [post](http://goo.gl/KUVCDu), [codelab](http://g.co/codelabs/gmail-add-ons), [source](https://github.com/googleworkspace/gmail-add-on-codelab) | Using Gmail Add-ons to scan receipts in your inbox to expedite expense reporting | Apps Script, Gmail API


#### Google Slides API
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/8LSUbKZq4ZY/default.jpg)](https://youtu.be/8LSUbKZq4ZYsAsi9QRgWuI) | Replacing text & images in Google Slides | [post](http://goo.gl/o6EFwk) | Perform the equivalent of a "slide deck template mail-merge" | Slides API
[![Watch video](https://i.ytimg.com/vi/_O2aUCJyCoQ/default.jpg)](https://youtu.be/_O2aUCJyCoQ) | Formatting text in Slides | [post](http://goo.gl/p4Jqvj) | Basic text-formatting in slide decks | Slides API
[![Watch video](https://i.ytimg.com/vi/sAsi9QRgWuI/default.jpg)](https://youtu.be/sAsi9QRgWuIZ5G0luBohCg) | Adding text & shapes to Google Slides | [post](http://goo.gl/WmRjYP) | Adding objects to slide decks | Slides API
[![Watch video](https://i.ytimg.com/vi/rTDz-Zcn7yk/default.jpg)](https://youtu.be/rTDz-Zcn7yk) | Generating Google Slides from images | [post](http://goo.gl/sYL5AM) | Auto-generating slides in a deck based on a set of images | Apps Script
[![Watch video](https://i.ytimg.com/vi/mKuINIBrR1g/default.jpg)](https://youtu.be/mKuINIBrR1g) | Making progress (bars) with Slides Add-ons | [post](http://goo.gl/69EJVw) | Adds a "progress bars" feature to Google Slides | Apps Script


#### Google Chat API and bot/app platform
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/ESSB3GvE9e0/default.jpg)](https://youtu.be/ESSB3GvE9e0) | The bots are coming! | [post](http://goo.gl/jt3FqK) | Developing chat bots/apps | Chat API
[![Watch video](https://i.ytimg.com/vi/ThKvlgnLyDk/default.jpg)](https://youtu.be/ThKvlgnLyDk) | Asynchronous messages in Google Chat | [post](http://bit.ly/2KvUvVK) | Sending asynchronous/out-of-band messages | Chat API


#### Google Forms API
Video | Title | Link(s) | Description | Other featured APIs/tools
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/L33hMxuoFtM/default.jpg)](https://youtu.be/L33hMxuoFtM) | Auto-generating Google Forms | [post](http://goo.gl/EK5edG) | How to automatically generate Google Forms | Apps Script


### GWS and GCP interoperability
Video | Title | Link(s) | Description | Relevant API(s), product(s), feature(s)
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/vyIap827rHs/default.jpg)](https://youtu.be/vyIap827rHs) | File Storage in the Cloud | _(n/a)_ | Essentially Google Drive vs. Cloud Storage | Google Drive, Google Cloud Storage, Google Cloud Persistent Disk
[![Watch video](https://i.ytimg.com/vi/BkaywE91KvM/default.jpg)](https://youtu.be/BkaywE91KvM) | Code that final mile: from big data analysis to slide presentation | [post](http://bit.ly/2O9KqDd), [codelab](http://g.co/codelabs/bigquery-sheets-slides), [source](http://github.com/wescpy/bigquery-sheets-slides) | Pushing BigQuery results to spreadsheets & slide decks | Apps Script, BigQuery, Sheets & Slides APIs
[![Watch video](https://i.ytimg.com/vi/1P6AXrUYprY/default.jpg)](https://youtu.be/1P6AXrUYprY) | Better together: How Google Cloud makes Google Workspace better for you | _(n/a)_ | Using GCP and GWS APIs in the same app(s) | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/w1i6biBZucY/default.jpg)](https://youtu.be/w1i6biBZucY) | Build WIth ALL of Cloud: GCP & GWS (formerly G Suite) Interoperability | _(n/a)_ | Using GCP & GWS APIs in case study/demo app(s), a Cloud Next '19 featured presentation | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/mR1MLi-_biU/default.jpg)](https://youtu.be/mR1MLi-_biU) | GWS (formerly G Suite) + GCP: Building Serverless Applications with All of Google Cloud | _(n/a)_ | Using GCP & GWS APIs in case study/demo app(s), a Cloud Next '18 featured presentation | _(tbd)_


### GCP serverless platforms (App Engine, Cloud Functions, Cloud Run)
Video | Title | Link(s) | Description | Relevant API(s), product(s), feature(s)
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/gle26fT28Bw/default.jpg)](https://youtu.be/gle26fT28Bw) | Picking the right serverless platform | [post](https://cloud.google.com/blog/topics/developers-practitioners/calling-google-apis-serverless-part-i-cloud-apis?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_nebservconcept_neb_202007) | How to choose between serverless platforms | App Engine, Cloud Functions, Cloud Run
[![Watch video](https://i.ytimg.com/vi/5qOwYSCb1Gg/default.jpg)](https://youtu.be/5qOwYSCb1Gg) | Top 3 pain points for serverless developers | _(n/a)_ | The biggest hangups/headaches for serverless developers | _(tbd)_
[![Watch video](https://i.ytimg.com/vi/ertbL2Rxbvk/default.jpg)](https://youtu.be/ertbL2Rxbvk) | How to design a serverless app | _(n/a)_ | How to design the backend/server-side for serverless apps | Cloud Run
[![Watch video](https://i.ytimg.com/vi/eTotLOVR7MQ/default.jpg)](https://youtu.be/eTotLOVR7MQ) | Deploy the same app to App Engine, Cloud Functions, and Cloud Run | [post](http://goo.gle/2Y0ph5q), _multiple codelabs below_, [Python source](https://github.com/wescpy/nebulous-serverless/tree/main/cloud/python), [Node.js source](https://github.com/wescpy/nebulous-serverless/tree/main/cloud/nodejs) | Can you deploy the same app to all platforms **with no code changes**? | App Engine, Cloud Functions, Cloud Run
[![Watch video](https://i.ytimg.com/vi/Px7RQWinK-s/default.jpg)](https://youtu.be/Px7RQWinK-s) | Developing Scalable Apps with Google App Engine | _(n/a)_ | App Engine product overview, part of the "Ask the Experts" series for developers | App Engine
[![Watch video](https://i.ytimg.com/vi/LhzDB8g1-FQ/default.jpg)](https://youtu.be/LhzDB8g1-FQ) | Google App Engine | _(n/a)_ | Product overview, a Google Developers Day - Berlin 2011 featured presentation | App Engine
[![Watch video](https://i.ytimg.com/vi/6TZ0e57pdZQ/default.jpg)](https://youtu.be/6TZ0e57pdZQ) | Google App Engine Overview | _(n/a)_ | Product overview, a Google I/O BootCamp 2011 featured presentation | App Engine
[![Watch video](https://i.ytimg.com/vi/ul1cGarS23M/default.jpg)](https://youtu.be/ul1cGarS23M) | How to use Cloud Run "always-on" CPU allocation for background work | [post](https://cloud.google.com/blog/topics/developers-practitioners/use-cloud-run-always-cpu-allocation-background-work) | Weather alerting Cloud Run app; "Always-on CPU" case study | Cloud Run, Cloud Datastore API
[![Watch video](https://i.ytimg.com/vi/eZj7uM9HaMg/default.jpg)](https://youtu.be/eZj7uM9HaMg) | Change the world in 10 lines of code | _(n/a)_ | Explores how you can change the world with [inbound email processing](https://cloud.google.com/appengine/docs/standard/services/mail/receiving-mail-with-mail-api) | App Engine

#### Nebulous serverless codelabs (Deploy the same app to App Engine, Cloud Functions, and Cloud Run)
Deployment | Python 2 | Python 3 | Node.js
--- | --- | --- | ---
Local/hosted Flask|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-flask?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservflask_sms_201020&utm_content=-) | _same as Python 2_ | [codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-nodejs?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservnodejs_sms_201130&utm_content=-)
App Engine|^[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gae2?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgae2_sms_201020&utm_content=-)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gae3?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgae3_sms_201020&utm_content=-) | _same as local/hosted_
Cloud Functions| _N/A_ |[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcf?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcf_sms_201020&utm_content=-) | _same as local/hosted_
Cloud Run (Docker)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcr2?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcr2_sms_201020&utm_content=-)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcr3?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcr3_sms_201020&utm_content=-) | _same as local/hosted_
Cloud Run (Buildpacks)| _N/A_ |[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcrbp?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcrbp_sms_201020&utm_content=-) | _same as local/hosted_

^ — not recommended as of Jan 2024 as developers can no longer deploy Python 2 apps to App Engine (see sidebar above)

#### Google App Engine (GAE) migration from 1st-gen platform
Video | Title | Link(s) | Description | Relevant non-App Engine API(s), product(s), feature(s)
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/loZt1AabFF0/default.jpg)](https://youtu.be/loZt1AabFF0) | Migrating from App Engine webapp2 to Flask | [post](http://goo.gle/3qVFpit), [codelab](http://g.co/codelabs/pae-migrate-flask), [Python 3 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod1b-flask), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod1-flask) | Migrating (web) frameworks for long-time App Engine developers
[![Watch video](https://i.ytimg.com/vi/KP1XinYiXfk/default.jpg)](https://youtu.be/KP1XinYiXfk) | Migrating from App Engine ndb to Cloud NDB| [post](http://goo.gle/3hT1xHi), [codelab](http://g.co/codelabs/pae-migrate-cloudndb), [Python 3 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod2b-cloudndb), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod2a-cloudndb) | How to slightly alter NDB access for better portability for long-time App Engine developers | Cloud NDB API
[![Watch video](https://i.ytimg.com/vi/KCwVNRSE3Eg/default.jpg)](https://youtu.be/KCwVNRSE3Eg) | Google Cloud NDB to Cloud Datastore migration | [post](http://goo.gle/37gZ43s), [codelab](http://g.co/codelabs/pae-migrate-datastore), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod3b-datastore), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod3a-datastore) | Migrating to the "new" Datastore API for long-time App Engine developers | Cloud NDB & Cloud Datastore APIs
[![Watch video](https://i.ytimg.com/vi/uI1mzwtx4ZM/default.jpg)](https://youtu.be/uI1mzwtx4ZM) | Migrating from App Engine to Cloud Run with Docker | [post](http://goo.gle/3geAqFs), [codelab](http://g.co/codelabs/pae-migrate-rundocker), [Python 3 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod4b-rundocker), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod4a-rundocker) | Migrating apps to Cloud Run with Docker for long-time App Engine developers | Cloud Run
[![Watch video](https://i.ytimg.com/vi/VP3g2OZYXPE/default.jpg)](https://youtu.be/VP3g2OZYXPE) | Migrating from App Engine to Cloud Run with Cloud Buildpacks | [post](http://goo.gle/3t3uyUN), [codelab](http://g.co/codelabs/pae-migrate-runbldpks), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod5-runbldpks) | Migrating apps to Cloud Run **without** Docker (with Buildpacks) for long-time App Engine developers | Cloud Run
[![Watch video](https://i.ytimg.com/vi/wNs36kukVOQ/default.jpg)](https://youtu.be/wNs36kukVOQ) | Migrating from Cloud Datastore to Cloud Firestore | _(n/a)_ | Optional/unnecessary migration from Datastore to Firestore APIs for long-time App Engine developers | Cloud Datastore & Cloud Firestore APIs
[![Watch video](https://i.ytimg.com/vi/JuWl8Q7_1FE/default.jpg)](https://youtu.be/JuWl8Q7_1FE) | How to use App Engine push queues in Flask apps | [post](http://goo.gle/3zQ8ler), [codelab](http://g.co/codelabs/pae-migrate-gaetasks), [Python 3 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod7b-gaetasks), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod7-gaetasks) | How to use (push) Task Queues in Flask apps for long-time App Engine developers
[![Watch video](https://i.ytimg.com/vi/JbTJFUmc5_A/default.jpg)](https://youtu.be/JbTJFUmc5_A) | Migrating App Engine push queues to Cloud Tasks | [post](http://goo.gle/3jmpNSr), [codelab](http://g.co/codelabs/pae-migrate-cloudtasks), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod8-cloudtasks) | Migrating from (push) Task Queues to Cloud Tasks for long-time App Engine developers | Cloud Tasks API
[![Watch video](https://i.ytimg.com/vi/dnKwYX8FbjE/default.jpg)](https://youtu.be/dnKwYX8FbjE) | Refactoring a Python 2 Cloud NDB app to Python 3 & Cloud Firestore | [codelab](http://g.co/codelabs/pae-migrate-py3dstasks), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod9-py3dstasks) | Case study: double migration from Python 2 to 3 and Cloud NDB to Cloud Firestore for long-time App Engine developers | Cloud NDB & Cloud Firestore APIs
[![Watch video](https://i.ytimg.com/vi/SCnF0fdfZTM/default.jpg)](https://youtu.be/SCnF0fdfZTM) | Migrating from App Engine to Cloud Functions | [post](https://t.co/qgZGxIdEnK), [codelab](http://g.co/codelabs/pae-migrate-functions), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod11-functions) | Breaking up monolithic apps into Cloud Functions (Gen 1) microservices for long-time App Engine developers | Cloud Functions
[![Watch video](https://i.ytimg.com/vi/WPI-7SXMg30/default.jpg)](https://youtu.be/WPI-7SXMg30) | How to use App Engine Memcache in Flask apps | [post](http://goo.gle/3lnCugx), [codelab](http://g.co/codelabs/pae-migrate-memcache), [Python 3 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod12b-memcache), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod12-memcache) | Using Memcache in Flask apps for improved portability for long-time App Engine developers
[![Watch video](https://i.ytimg.com/vi/lyqSTsLYBOU/default.jpg)](https://youtu.be/lyqSTsLYBOU) | Migrating App Engine memcache to Cloud Memorystore | [post](http://goo.gle/3zBOcfX), [codelab](http://g.co/codelabs/pae-migrate-memorystore), [Python 3 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod13b-memorystore), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod13a-memorystore) | Migrating from `memcache` to Cloud Memorystore for Redis for long-time App Engine developers | Cloud Memorystore for Redis API
[![Watch video](https://i.ytimg.com/vi/I4VWsB7uw_A/default.jpg)](https://youtu.be/I4VWsB7uw_A) | How to use App Engine blobstore in Flask apps | [post](http://goo.gle/3vgkzxJ), [codelab](http://g.co/codelabs/pae-migrate-blobstore), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod15-blobstore) | Using Blobstore in Flask apps for better portability for long-time App Engine developers
[![Watch video](https://i.ytimg.com/vi/7xezFiVc8xg/default.jpg)](https://youtu.be/7xezFiVc8xg) | Migrating App Engine Blobstore to Cloud Storage | [post](http://goo.gle/3Angr1K), [codelab](http://g.co/codelabs/pae-migrate-cloudstorage), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod16-cloudstorage) | Migrating Blobstore API usage to Cloud Storage for long-time App Engine developers | Cloud Storage
[![Watch video](https://i.ytimg.com/vi/Tyyv4_Khyk0/default.jpg)](https://youtu.be/Tyyv4_Khyk0) | Extending support for App Engine bundled services: Part 1 | [post](http://goo.gle/3Nry9Gt), [codelab](http://g.co/codelabs/pae-migrate-bundled), [source](https://github.com/wescpy/migrate-python2-appengine/blob/master/mod1b-flask) | Accessing App Engine bundled services with its Gen2 platform for long-time App Engine developers
[![Watch video](https://i.ytimg.com/vi/H7BShZm7wf4/default.jpg)](https://youtu.be/H7BShZm7wf4) | How to use App Engine Task Queue pull tasks | [post](http://goo.gle/3AVLyRO), [codelab](http://g.co/codelabs/pae-migrate-gaepull), [source](https://github.com/wescpy/migrate-python2-appengine/tree/master/mod18-gaepull) | Using pull tasks in Flask apps for long-time App Engine developers
[![Watch video](https://i.ytimg.com/vi/mD7emln-z_Q/default.jpg)](https://youtu.be/mD7emln-z_Q) | Migrating App Engine pull tasks to Cloud Pub/Sub | [post](http://goo.gle/3hqu1uD), [codelab](http://g.co/codelabs/pae-migrate-pubsub), [source](https://github.com/wescpy/migrate-python2-appengine/tree/master/mod19-pubsub) | Migrating (pull) Task Queue to Cloud Pub/Sub for long-time App Engine developers | Cloud Pub/Sub
[![Watch video](https://i.ytimg.com/vi/UTjVF5TAN74/default.jpg)](https://youtu.be/UTjVF5TAN74) | How to use App Engine Users service in Flask apps | [post](http://goo.gle/3QlGCfG), [codelab](http://g.co/codelabs/pae-migrate-gaeusers), [source](https://github.com/wescpy/migrate-python2-appengine/tree/master/mod20-gaeusers) | Using the Users API for authentication in Flask apps for long-time App Engine developers |
[![Watch video](https://i.ytimg.com/vi/Ofo0qMgGesE/default.jpg)](https://youtu.be/Ofo0qMgGesE) | Migrate App Engine Users service to Cloud Identity Platform | [post](https://https://developers.googleblog.com/2023/01/migrating-from-app-engine-users-to-cloud-identity-module-21.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_mgridenplat_sms_202119), [codelab](http://g.co/codelabs/pae-migrate-idenplat), [Python 3 source](https://github.com/wescpy/migrate-python2-appengine/tree/master/mod21b-idenplat), [Python 2 source](https://github.com/wescpy/migrate-python2-appengine/tree/master/mod21a-idenplat) | Migrating off the Users API to Cloud Identity Platform & Firebase Auth for long-time App Engine developers | Cloud Identity Platform & Cloud Resource Manager APIs
[![Watch video](https://i.ytimg.com/vi/ZhEBSvnz_BQ/default.jpg)](https://youtu.be/ZhEBSvnz_BQ) | Extending support for App Engine bundled services: Part 2 | _(n/a)_ | Using App Engine bundled services requiring more effort with its Gen2 platform for long-time App Engine developers |


### Miscellaneous
Video | Title | Link(s) | Description | Relevant API(s), product(s), feature(s)
--- | --- | --- | --- | ---
[![Watch video](https://i.ytimg.com/vi/KKQS8EDG1P4/default.jpg)](https://youtu.be/KKQS8EDG1P4) | Python at Google | _(n/a)_ | How Google & YouTube use Python, a Google I/O 2011 featured presentation delivered with the inventor of Python, Guido van Rossum
[![Watch video](https://i.ytimg.com/vi/D7BpG0e73-Y/default.jpg)](https://youtu.be/D7BpG0e73-Y) | Faculty Summit: Create Your Own Codelab | _(n/a)_ | How to create "codelabs" (self-paced, hands-on tutorials) | [`claat` codelab generator tool](https://github.com/googlecodelabs/tools)
[![Watch video](https://i.ytimg.com/vi/ja4E9Dzr0Gw/default.jpg)](https://youtu.be/ja4E9Dzr0Gw) | Easy path to Machine Learning | _(n/a)_ | How to get up-to-speed with AI/ML by learning the GCP Vertex AI "building block" APIs backed by single-task, pre-trained models | GCP Vertex AI: Cloud Vision API & Cloud Natural Language APIs
[![Watch video](https://i.ytimg.com/vi/xuPKrjJ8Ijs/default.jpg)](https://youtu.be/xuPKrjJ8Ijs) | Powering the next killer app with GCP | _(n/a)_ | General intro to GCP


## Relevant playlists
Most of the videos above belong to one of these playlists:

Video Series | Relevant Google description | Intended audience (but open to all)
--- | --- | ---
[Launchpad Online](http://goo.gl/kFMUa6) | [post](https://developers.googleblog.com/2014/11/accelerate-business-growth-with-startup.html) | startups
[Workspace (GWS; formerly G Suite) Dev Show](http://goo.gl/JpBQ40) | [Tweet](https://twitter.com/googledevs/status/796383831188275200) | Gmail, Google Drive, Docs, Sheets, etc. developers
[Serverless Migration Station](http://bit.ly/3xk2Swi) | [post](http://goo.gle/3h0GnFw) | Python 2 App Engine developers seeking to upgrade
[Google Cloud for Student Developers](http://goo.gle/GCPStudent) | [page](https://cloud.google.com/edu/students) | student developers
[Google Apps Script](http://youtube.com/playlist?list=PL2pQQBHvYcs2jn6h9oBs9q0aShbqLdgb8) | (deprecated) [page](https://web.archive.org/web/20220929161227/https://developers.google.com/apps-script/guides/videos) | Serverless platform for enhancing, extending, and automating GWS, other Google, and _non-Google_ resources
Google Drive _(tbd)_ | [page](http://developers.google.com/drive/web/videos) | Google Drive API
[Google Slides](http://bit.ly/wescpy-slides-api-vids) | [page](http://developers.google.com/slides/videos) | Google Slides API
[Google Sheets](http://bit.ly/wescpy-sheets-api-vids) | [page](http://developers.google.com/sheets/api/videos) | Google Sheets API
Google Chat _(tbd)_ | (deprecated) [page](https://web.archive.org/web/20210618140718/https://developers.google.com/chat#featured-videos) | Google (formerly Hangouts) Chat bot & app platform
