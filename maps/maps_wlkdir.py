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
#
# FILE:    maps_wlkdir.py
# POST:    dev.to/wescpy/explore-the-world-with-google-maps-apis-lhj

'''
maps_wlkdir.py -- get Google Maps walking directions
'''
from __future__ import print_function
from datetime import datetime
import googlemaps
from html2text import html2text
from settings import API_KEY

ADDRESSES = ('111 8th Ave, New York', '76 9th Ave')
GMAPS = googlemaps.Client(key=API_KEY)
rsp = GMAPS.directions(*ADDRESSES, mode='walking', departure_time=datetime.now())
dirs = rsp[0]['legs'][0]

print('** Walking directions...')
print('STARTING from:', dirs['start_address'])
print('CONCLUDING at:', dirs['end_address'])
print('DISTANCE:', dirs['distance']['text'])
print('DURATION:', dirs['duration']['text'])
print('DIRECTIONS:')
for i, step in enumerate(dirs['steps']):
    print('\t%d.' % (i+1), html2text(
        step['html_instructions']).strip().replace('\n\n', '\n\t'))
