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

'''
transnatlang-apikey-old.py -- GCP Natural Language & Translation APIs demo
'''
from __future__ import print_function
from googleapiclient import discovery
from settings import API_KEY

# Text to process
_TEXT = '''\
    Google, headquartered in Mountain View, unveiled the new Android
    phone at the Consumer Electronics Show. Sundar Pichai said
    in his keynote that users love their new Android phones.
'''
TEXT = ' '.join(_TEXT.strip().split())
LINE = '-' * 60

# Display text to process
print('TEXT:')
print(TEXT)
print(LINE)

# Create API clients/endpoints
NL = discovery.build('language',  'v1', developerKey=API_KEY)
TL = discovery.build('translate', 'v2', developerKey=API_KEY)

# Detect text sentiment
BODY = {'content': TEXT, 'type': 'PLAIN_TEXT'}
sent = NL.documents().analyzeSentiment(
        body={'document': BODY}).execute().get('documentSentiment')
print('\nSENTIMENT: score (%.2f), magnitude (%.2f)' % (
        sent['score'], sent['magnitude']))
print(LINE)

# Categorize text
print('\nCATEGORIES:')
categories = NL.documents().classifyText(
        body={'document': BODY}).execute().get('categories')
for cat in categories:
    print('* %s (%.2f)' % (cat['name'][1:], cat['confidence']))
print(LINE)

# Translate text to Spanish
TARGET = 'es'
txln = TL.translations().list(
        q=TEXT, target=TARGET).execute().get('translations')[0]
print('\nTRANSLATION to %r:\n%s' % (TARGET, txln['translatedText']))
