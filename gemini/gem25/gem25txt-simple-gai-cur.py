# Copyright 2025 CyberWeb Consulting LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# FILE:    gem25txt-simple-gai-cur.py
# POST:    bit.ly/4kFkmLm

from google import genai
from settings import API_KEY

PROMPT = 'Describe a cat in a few sentences'
MODEL = 'gemini-2.5-flash'
print('** GenAI text: %r model & prompt %r\n' % (MODEL, PROMPT))

GENAI = genai.Client(api_key=API_KEY)
# GENAI = genai.Client()  # use API key in GEMINI_API_KEY env var
response = GENAI.models.generate_content(model=MODEL, contents=PROMPT)
print(response.text)
