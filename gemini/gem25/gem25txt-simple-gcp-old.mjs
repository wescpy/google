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
// FILE:    gem25txt-simple-gcp-old.mjs
// POST:    TBD

import 'dotenv/config';
import { VertexAI } from "@google-cloud/vertexai";

const PROMPT = 'Describe a cat in a few sentences';
const MODEL = 'gemini-2.5-flash';
console.log(`** GenAI text: '${MODEL}' model & prompt '${PROMPT}'\n`);

const CONFIG = JSON.parse(process.env.GCP_METADATA);
const VERTEXAI = new VertexAI(CONFIG);
const GENAI = VERTEXAI.getGenerativeModel({ model: MODEL });

async function main() {
  const result = await GENAI.generateContent(PROMPT);
  console.log(result.response.candidates[0].content.parts[0].text);
}

main();
