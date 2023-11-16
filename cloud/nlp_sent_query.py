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
from googleapiclient import discovery
from settings import API_KEY

TEXT = '''Google, headquartered in Mountain View, unveiled the new
Android phone at the Consumer Electronics Show. Sundar Pichai said
in his keynote that users love their new Android phones.'''
NLP = discovery.build('language', 'v1', developerKey=API_KEY)

print('TEXT:', TEXT)
data = {'type': 'PLAIN_TEXT', 'content': TEXT}
sent = NLP.documents().analyzeSentiment(
        body={'document': data}).execute().get('documentSentiment')
print('\nSENTIMENT: score (%.2f), magnitude (%.2f)' % (
        sent['score'], sent['magnitude']))
