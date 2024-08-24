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
#
# FILE:    yt_video_query.py
# POST:    dev.to/googleworkspace/getting-started-using-google-apis-api-keys-part-2-38i6
# POST:    dev.to/wescpy/TBD

from __future__ import print_function
from googleapiclient import discovery
from settings import API_KEY

QUERY = 'python -snake'
YOUTUBE = discovery.build('youtube', 'v3', developerKey=API_KEY)

print('\n** Searching for %r videos...' % QUERY)
res = YOUTUBE.search().list(q=QUERY, type='video',
        part='id,snippet').execute().get('items', [])
for item in res:
    print('http://youtu.be/%s\t%s' % (
            item['id']['videoId'], item['snippet']['title'][:48]))
