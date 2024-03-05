# POST:         https://dev.to/wescpy/export-google-docs-as-pdf-without-the-docs-api-9o4...
# FILE:         drive_export_doc_pdf.py
# COPYRIGHT:    (c)2024 CyberWeb Consulting LLC
# LICENSE:      apache.org/licenses/LICENSE-2.0

from __future__ import print_function
import os

from google.auth.transport.requests import Request
from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery

SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
CLNT_ID_SCRT = 'client_secret.json'
OAUTH_TOKENS = 'storage.json'
MIMETYPE = 'application/pdf'
FILENAME = 'Merged form letter'

# check credentials from locally-stored OAuth2 tokens file; either
# refresh expired tokens or run flow to get new pair & create API client
creds = None
if os.path.exists(OAUTH_TOKENS):
    creds = credentials.Credentials.from_authorized_user_file(OAUTH_TOKENS)
if not (creds and creds.valid):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLNT_ID_SCRT, SCOPES)
        creds = flow.run_local_server()
with open(OAUTH_TOKENS, 'w') as token:
    token.write(creds.to_json())
DRIVE = discovery.build('drive', 'v3', credentials=creds)

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
