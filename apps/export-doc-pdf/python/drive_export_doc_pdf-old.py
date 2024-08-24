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
# FILE:    drive_export_doc_pdf-old.py
# POST:    dev.to/wescpy/export-google-docs-as-pdf-without-the-docs-api-9o4

from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
CLNT_ID_SCRT = 'client_secret.json'
OAUTH_TOKENS = 'storage.json'
MIMETYPE = 'application/pdf'
FILENAME = 'Merged form letter'

# check credentials from locally-stored OAuth2 tokens file; either
# refresh expired tokens or run flow to get new pair & create API client
store = file.Storage(OAUTH_TOKENS)
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLNT_ID_SCRT, SCOPES)
    creds = tools.run_flow(flow, store)
DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

# query API; download if found and non-empty
res = DRIVE.files().list(q="name='%s'" % FILENAME,
         fields='files(id)', pageSize=1).execute().get('files')
if res:
    print('** Downloading %r' % FILENAME)
    file_id = res[0]['id']
    data = DRIVE.files().export(fileId=file_id, mimeType=MIMETYPE).execute()
    if data:
        with open('%s.pdf' % FILENAME, 'wb') as fh:
            fh.write(data)
