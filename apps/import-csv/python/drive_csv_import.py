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
# FILE:    drive_csv_import.py
# POST:    dev.to/googleworkspace/import-csv-to-google-sheets-without-the-sheets-api-20g1

from __future__ import print_function
import os

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery
from google.oauth2 import credentials

# check credentials from locally-stored OAuth2 tokens file; either
# refresh expired tokens or run flow to get new pair & create API client
creds = None
SCOPES = 'https://www.googleapis.com/auth/drive.file'
TOKENS = 'storage.json'  # where to store access & refresh tokens
if os.path.exists(TOKENS):
    creds = credentials.Credentials.from_authorized_user_file(TOKENS)
if not (creds and creds.valid):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
        creds = flow.run_local_server()
with open(TOKENS, 'w') as token:
    token.write(creds.to_json())
DRIVE = discovery.build('drive', 'v3', credentials=creds)

# filenames & MIMEtypes
DST_FILENAME = 'inventory'
SRC_FILENAME = DST_FILENAME + '.csv'
SHT_MIMETYPE = 'application/vnd.google-apps.spreadsheet'

# import CSV file to Drive, converting to Google Sheets format
METADATA = {'name': DST_FILENAME, 'mimeType': SHT_MIMETYPE}
rsp = DRIVE.files().create(
        body=METADATA, media_body=SRC_FILENAME).execute()
if rsp:
    print('Imported %r as Sheets to %r (file ID: %s)' % (
            SRC_FILENAME, DST_FILENAME, rsp['id']))
