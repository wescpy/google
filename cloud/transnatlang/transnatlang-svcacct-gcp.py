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
transnatlang-svcacct-gcp.py -- GCP Natural Language & Translation APIs demo (Python 2/3-compatible)
'''
from __future__ import print_function
import sys
from google.cloud import language_v1 as language, translate_v2 as translate

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
NL = language.LanguageServiceClient()
TL = translate.Client()

# Detect text sentiment
TYPE = 'type_' if sys.version_info.major == 3 else 'type'
BODY = {'content': TEXT, TYPE: language.types.Document.Type.PLAIN_TEXT}
sent = NL.analyze_sentiment(document=BODY).document_sentiment
print('\nSENTIMENT: score (%.2f), magnitude (%.2f)' % (
        sent.score, sent.magnitude))
print(LINE)

# Categorize text
print('\nCATEGORIES:')
categories = NL.classify_text(document=BODY).categories
for cat in categories:
    print('* %s (%.2f)' % (cat.name[1:], cat.confidence))
print(LINE)

# Translate text to Spanish
TARGET = 'es'
txlns = TL.translate(TEXT, TARGET)
txln = txlns[0] if isinstance(txlns, list) else txlns
print('\nTRANSLATION to %r:\n%s' % (TARGET, txln['translatedText']))
