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
maps_tzone.py -- geocode address and get Google Maps time zone
'''
from __future__ import print_function
import googlemaps
from settings import API_KEY

ADDRESS = '1600 Amphitheatre Pkwy 94043'
GMAPS = googlemaps.Client(key=API_KEY)
rsp = GMAPS.geocode(ADDRESS)[0]['geometry']['location']
rsp = GMAPS.timezone((rsp['lat'], rsp['lng']))

offset = rsp['rawOffset'] + rsp['dstOffset']
sign = '-' if offset < 0 else '+'
offset, frac = divmod(abs(offset), 3600)
frac_str = str(round(frac/3600, 2))[1:] if frac else ''
tz_abbr = ''.join(c[0] for c in rsp['timeZoneName'].split())
print('** Time zone for %r:' % ADDRESS, rsp['timeZoneId'],
        '(%s/GMT%s%s%s)' % (tz_abbr, sign, offset, frac_str))
