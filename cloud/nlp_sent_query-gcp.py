# Copyright 2023 CyberWeb Consulting LLC
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

from __future__ import print_function
from google.cloud import language_v1 as language
from settings import API_KEY

TEXT = '''Google, headquartered in Mountain View, unveiled the new
Android phone at the Consumer Electronics Show. Sundar Pichai said
in his keynote that users love their new Android phones.'''
NLP = language.LanguageServiceClient(client_options={'api_key': API_KEY})
#NLP = language.LanguageServiceClient(
#        client_options={'api_key': API_KEY,})# "quota_project_id": quota_project_id}

data = {'content': TEXT, 'type_': language.Document.Type.PLAIN_TEXT}
print('TEXT:', TEXT)
sent = NLP.analyze_sentiment(request={'document': data}).document_sentiment
print('\nSENTIMENT: score (%.2f), magnitude (%.2f)' % (
        sent.score, sent.magnitude))
