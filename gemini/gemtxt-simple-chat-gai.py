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
# FILE:    gemtxt-simple-chat-gai.py
# POST:    dev.to/wescpy/gemini-api-102-next-steps-beyond-hello-world-1pb7

import google.generativeai as genai
from settings import API_KEY

PROMPTS = ('Describe a cat in a few sentences',
    "Since you're now a feline expert, what are the top three "
    'most friendly cat breeds for a family with small children?'
)
MODEL = 'gemini-1.5-flash'
print('** GenAI text: %r model\n' % MODEL)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL)
chat = model.start_chat()
for prompt in PROMPTS:
    print('\nUSER:', prompt)
    response = chat.send_message(prompt)
    print('\nMODEL:', response.text)
print()
