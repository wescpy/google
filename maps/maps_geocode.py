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
# FILE:    maps_geocode.py
# POST:    dev.to/wescpy/explore-the-world-with-google-maps-apis-lhj

'''
maps_geocode.py -- geocode address in Google Maps
'''
from __future__ import print_function
import googlemaps
from settings import API_KEY

ADDRESS = '1600 Amphitheatre Pkwy 94043'
GMAPS = googlemaps.Client(key=API_KEY)
rsp = GMAPS.geocode(ADDRESS)[0]
geo = rsp['geometry']['location']
print('** Geocode for %r: (%s, %s)' % (ADDRESS, geo['lat'], geo['lng']))
