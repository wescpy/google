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
# FILE:    gem20-image.py
# POST:    dev.to/wescpy/TBD

from io import BytesIO
from PIL import Image
from google import genai
from settings import GOOGLE_API_KEY

# set constants
MODEL = 'gemini-2.0-flash-exp'
GENAI = genai.Client(api_key=GOOGLE_API_KEY)
#GENAI = genai.Client()  # read from GOOGLE_API_KEY env var
CONFIG = genai.types.GenerateContentConfig(
        response_modalities=['Text', 'Image'])
PROMPT = 'Create an image of a cat in a spacesuit driving a moon buggy.' \
            ' Also return a caption for the image.'
FILENAME = 'spacecat.png'

# Generate image with Gemini 2
print(f"MODEL:\t\t'{MODEL}'\nPROMPT:\t\t'{PROMPT}\n")
response = GENAI.models.generate_content(
        model=MODEL, contents=PROMPT, config=CONFIG)

# Process results
for part in response.candidates[0].content.parts:
    if part.text:
        print(f"CAPTION:\t{part.text.strip().replace('**Caption:** ', '')}")
    elif part.inline_data:
        image = Image.open(BytesIO((part.inline_data.data)))
        image.save(FILENAME)
        print(f'IMAGE:\t\t{FILENAME}')
