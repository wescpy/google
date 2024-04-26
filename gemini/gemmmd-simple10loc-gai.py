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

from PIL import Image
import google.generativeai as genai
from settings import API_KEY

IMG = 'dome-waterfall.jpg'  # SOURCE: Wesley Chun (CC-BY-4.0)
DATA = Image.open(IMG)
PROMPT = "Where is this located, and what's the waterfall's name?"
MODEL = 'gemini-1.0-pro-vision-latest'
print('** GenAI multimodal: %r model & prompt %r\n' % (MODEL, PROMPT))

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL)
response = model.generate_content((PROMPT, DATA))
print(response.text)
