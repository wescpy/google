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
# FILE:    md2docs-old.py
# POST:    dev.to/googleworkspace/building-a-basic-markdown-to-google-docs-converter-1220

from __future__ import print_function
import re

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

FILENAME = 'quickbrownfox.md'  # change to your own Markdown file

# authorization code
SCOPES = 'https://www.googleapis.com/auth/documents'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
DOCS = discovery.build('docs', 'v1', http=creds.authorize(Http()))

def read_parse_md(fname):
    'parse Markdown, strip to plain text, create styling actions'
    # read Markdown content
    with open(fname, 'r') as f:
        content = f.read()

    # parse actions & remove tokens; convert to plain text
    matches = re.findall(r'(([_*])([^\2]+?)\2)', content)
    actions = []  # Markdown styling actions
    for match in matches:
        md, dl, pt = match      # MD string, delimiter, plain text string
        i = content.find(md)    # begin index for styling
        j = i + len(pt) + 1     # end index for styling
        content = content.replace(md, pt)   # replace MD with plain text
        action = 'bold' if dl == '*' else 'italic'  # Markdown action
        actions.append((action, i, j))      # add to styling actions
    return content, actions


def create_doc(fname):
    'create new & empty Google Doc and return file ID'
    return DOCS.documents().create(
            body={'title': fname}).execute().get('documentId')


def write_text(text, docs_id):
    'write text into Doc'
    requests = [{'insertText': {'location': {'index': 1}, 'text': text}}]
    DOCS.documents().batchUpdate(body={'requests': requests},
            documentId=docs_id, fields='').execute()


def format_text(actions, docs_id):
    'format text with requested Markdown styling'
    requests = [{
        'updateTextStyle': {
            'range': {'startIndex': i, 'endIndex': j},
            'textStyle': {style: True}, 'fields': style,
        }
    } for style, i, j in actions]
    DOCS.documents().batchUpdate(body={'requests': requests},
            documentId=docs_id, fields='').execute()


if __name__ == '__main__':
    text, actions = read_parse_md(FILENAME)
    print('** Parsed Markdown file %r & style actions' % FILENAME)
    docs_fn = FILENAME.replace('.md', '')  # remove MD file ext
    docs_id = create_doc(docs_fn)
    print('** Created %r (ID: %s)' % (docs_fn, docs_id))
    write_text(text, docs_id)
    print('** Inserted %r into document' % text)
    format_text(actions, docs_id)
    print('** Completed Markdown formatting in document:', actions)
