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
# FILE:    gem20-audio.py
# POST:    dev.to/wescpy/generate-audio-clips-with-gemini-20-flash-from-google-n0g

import asyncio
import contextlib
import wave

from google import genai
from settings import API_KEY

CLIENT = genai.Client(api_key=API_KEY, http_options={'api_version': 'v1alpha'})
MODEL = 'gemini-2.0-flash-exp'
CONFIG = {'generation_config': {'response_modalities': ['AUDIO']}}
PROMPT = 'Describe a cat in a few sentences'
FILENAME = 'whatacatis.wav'

@contextlib.contextmanager
def wave_file(filename, channels=1, rate=24000, sample_width=2):
    'set up .wav file writer'
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        yield wf

async def request_audio(prompt=PROMPT, filename=FILENAME):
    'request LLM generate audio file given prompt'
    print(f'\n** LLM prompt: "{prompt}"')
    async with CLIENT.aio.live.connect(model=MODEL, config=CONFIG) as session:
        with wave_file(filename) as f:
            await session.send(prompt, end_of_turn=True)
            async for response in session.receive():
                if response.data:
                    f.writeframes(response.data)
    print(f'** Saved audio to "{filename}"')

asyncio.run(request_audio())
