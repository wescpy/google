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
from pprint import pprint
from googleapiclient import discovery
from settings import API_KEY

SHEETS = discovery.build('sheets', 'v4', developerKey=API_KEY)
SHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
print('** Printing student database...')
pprint(SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID,
        range='Class Data', fields='values').execute().get('values', []))
