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
transnatlang-svcacct-gcp-async.py -- GCP Natural Language & Translation APIs demo (Python 3-only)
'''
import asyncio
import sys
from google.cloud import language_v1 as language, translate_v2 as translate

# Text to analyze
_TEXT: str = '''\
    Google, headquartered in Mountain View, unveiled the new Android
    phone at the Consumer Electronics Show. Sundar Pichai said
    in his keynote that users love their new Android phones.
'''
TEXT: str = ' '.join(_TEXT.strip().split())
LINE: str = '-' * 60

# Create API clients/endpoints
NL: language.LanguageServiceClient = language.LanguageServiceClient()
TL: translate.client.Client = translate.Client()
BODY: dict = {'content': TEXT, 'type_': language.types.Document.Type.PLAIN_TEXT}


async def sentAnalysis() -> None:
    'Detect text sentiment'
    sent = NL.analyze_sentiment(document=BODY)
    docsent = sent.document_sentiment
    print(f'\nSENTIMENT: score ({docsent.score:.2f}), magnitude ({docsent.magnitude:.2f}')
    print(LINE)


async def categorizeText() -> None:
    'Categorize text'
    print('\nCATEGORIES:')
    categories = NL.classify_text(document=BODY)
    for cat in categories.categories:
        print(f'* {cat.name[1:]} ({cat.confidence:.2f})')
    print(LINE)


async def translateText() -> None:
    'Translate text to Spanish'
    TARGET: str = 'es'
    txlns = TL.translate(TEXT, TARGET)
    txln = txlns[0] if isinstance(txlns, list) else txlns
    print(f"\nTRANSLATION to '{TARGET}':\n{txln['translatedText']}")


async def main() -> None:
    'Display text to analyze'
    print('TEXT:')
    print(TEXT)
    print(LINE)
    await sentAnalysis()
    await categorizeText()
    await translateText()


asyncio.run(main())
