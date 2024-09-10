# Copyright 2024 CyberWeb Consulting LLC
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
# FILE:    gemmmd-simple-url-chat-gai.py
# POST:    dev.to/wescpy/gemini-api-102-next-steps-beyond-hello-world-1pb7

from PIL import Image
import requests
import google.generativeai as genai
from settings import API_KEY

IMG_URL = 'https://google.com/services/images/section-work-card-img_2x.jpg'  # SOURCE: Google
IMG_RAW = Image.open(requests.get(IMG_URL, stream=True).raw)
PROMPTS = ('Describe the scene in this photo',
    'You are a marketing expert. If a company uses this photo in a '
    'press release, what product or products could they be selling?'
)
MODEL = 'gemini-1.5-flash'
print('** GenAI multimodal: %r model\n' % MODEL)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL)
messages = []
for prompt in PROMPTS:
    print('\nUSER:', prompt)
    messages.append({'role': 'user', 'parts': (prompt, DATA)})
    response = model.generate_content(messages)
    messages.append(response.candidates[0].content)
    print('\nMODEL:', response.text)
print()
