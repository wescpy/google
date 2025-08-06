# Copyright 2025 CyberWeb Consulting LLC
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
# FILE:    gmail_chatty_threads-old.py
# POST:    https://bit.ly/4ljSH2W

from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

# check credentials from locally-stored OAuth2 tokens file; either
# refresh expired tokens or run flow to get new pair & create API client
SCOPES = 'https://www.googleapis.com/auth/gmail.metadata'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

# scan your threads and individual msgs in each
threads = GMAIL.users().threads().list(userId='me').execute().get('threads', [])
for thread in threads:
    # process msgs for a thread
    tdata = GMAIL.users().threads().get(userId='me',
            id=thread['id'], format='metadata').execute()
    nmsgs = len(tdata['messages'])

    if nmsgs > 2:    # dump if <3 msgs in thread
        msg = tdata['messages'][0]['payload']
        subject = ''
        for header in msg['headers']:
            if header['name'] == 'Subject':
                subject = header['value']
                break
        if subject:  # dump if no Subject line
            print('-% 3d msgs: %s' % (nmsgs,
                    subject if len(subject)<45 else '%s...' % subject[:42],))
