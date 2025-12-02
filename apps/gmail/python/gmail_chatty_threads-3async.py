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
# FILE:    gmail_chatty_threads-3async.py
# POST:    bit.ly/4ljSH2W

import asyncio
import os
from typing import Any, Dict, List, Set, Optional

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow as InstAppFlow
from googleapiclient import discovery
from google.oauth2.credentials import Credentials

# check credentials from locally-stored OAuth2 tokens file; either
# refresh expired tokens or run flow to get new pair & create API client
creds: Optional[Credentials] = None
SCOPES: str = 'https://www.googleapis.com/auth/gmail.metadata'
TOKENS: str = 'storage.json'  # where to store access & refresh tokens
if os.path.exists(TOKENS):
    creds = Credentials.from_authorized_user_file(TOKENS)
if not (creds and creds.valid):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow: InstAppFlow = InstAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
        creds = flow.run_local_server()
with open(TOKENS, 'w') as token:
    token.write(creds.to_json())
GMAIL: Any = discovery.build('gmail', 'v1', credentials=creds)

async def proc_thread(thread: Dict[str, Any]) -> None:
    'process msgs for a thread'
    tdata: Dict[str, Any] = GMAIL.users().threads().get(
            userId='me', id=thread['id'], format='metadata').execute()
    nmsgs: int = len(tdata['messages'])

    if nmsgs > 2:    # dump if <3 msgs in thread
        msg: Dict[str, Any] = tdata['messages'][0]['payload']
        subject: str = ''
        for header in msg['headers']:
            if header['name'] == 'Subject':
                subject = header['value']
                break
        if subject:  # dump if no Subject line
            print(f'-{nmsgs: 3d} msgs: '
                  f'{subject if len(subject)<45 else "%s..." % subject[:42]}')

async def main() -> None:
    # scan your threads and individual msgs in each;
    # process each thread asynchronously
    threads: List[Dict[str, Any]] = GMAIL.users().threads().list(
            userId='me').execute().get('threads', [])
    tasks: Set[asyncio.Task[None]] = {
            asyncio.create_task(proc_thread(thread)) for thread in threads}
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
