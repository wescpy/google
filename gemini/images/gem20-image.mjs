// Copyright 2025 CyberWeb Consulting LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// FILE:    gem20-image.mjs
// POST:    dev.to/wescpy/TBD

import dotenv from 'dotenv';
import { GoogleGenAI } from '@google/genai';
import * as fs from 'node:fs';

// set constants
dotenv.config();
const MODEL = 'gemini-2.0-flash-exp';
const CONFIG = { responseModalities: ['Text', 'Image'] };
const PROMPT = 'Create an image of a cat in a spacesuit driving a moon buggy.'
                    + 'Also return a caption for the image.';
const FILENAME = 'spacecat.png';

async function main() {
  // Generate image with Gemini 2
  console.log(`** GenAI image: '${MODEL}' model & prompt '${PROMPT}'\n`);
  const GENAI = new GoogleGenAI({ apiKey: process.env.GOOGLE_API_KEY });
  const response = await GENAI.models.generateContent({
      model: MODEL,
      contents: PROMPT,
      config: CONFIG,
  });

  // Process results
  for (const part of response.candidates[0].content.parts) {
      if (part.text) {
          console.log(`    Generated text: ${part.text.trim()}`);
      } else if (part.inlineData) {
          const imageData = part.inlineData.data;
          const buffer = Buffer.from(imageData, 'base64');
          fs.writeFileSync(FILENAME, buffer);
          console.log(`    Image saved to: ${FILENAME}`);
      }
   }
}

main();
