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
// FILE:    gem25txt-simple-gcp-cur.js
// POST:    bit.ly/4kFkmLm

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');

const PROMPT = 'Describe a cat in a few sentences';
const MODEL = 'gemini-2.5-flash';
console.log(`** GenAI text: '${MODEL}' model & prompt '${PROMPT}'\n`);

const CONFIG = JSON.parse(process.env.GCP_METADATA);
const GENAI = new GoogleGenAI({ vertexai: true, ...CONFIG });
//const GENAI = new GoogleGenAI({ apiKey: process.env.API_KEY });  // use API key from .env

async function main() {
  const response = await GENAI.models.generateContent({
    model: MODEL,
    contents: PROMPT
  });
  console.log(response.text);
}

main();
