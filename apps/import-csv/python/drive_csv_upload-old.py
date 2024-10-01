# Copyright 2024 CyberWeb Consulting LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# Obtain a copy of the License at: apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# FILE:    drive_csv_upload-old.py
# POST:    dev.to/wescpy/

from __future__ import print_function
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# check credentials from locally-stored OAuth2 tokens file; either
# refresh expired tokens or run flow to get new pair & create API client
SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

# upload CSV file as-is with Drive API
FILENAME = 'inventory.csv'
METADATA = {'name': FILENAME}
rsp = DRIVE.files().create(
        body=METADATA, media_body=FILENAME).execute()
if rsp:
    print('Uploaded %r to Drive (file ID: %s)' % (
            FILENAME, rsp['id']))
