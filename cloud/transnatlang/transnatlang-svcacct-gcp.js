/**
 * Copyright 2024 CyberWeb Consulting LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// transnatlang-svcacct-gcp.js -- Cloud Natural Language & Translation APIs demo
const LanguageClient = require('@google-cloud/language');
const {Translate} = require('@google-cloud/translate').v2;

/** Text to process */
const TEXT = `Google, headquartered in Mountain View, unveiled
the new Android phone at the Consumer Electronics Show. Sundar
Pichai said in his keynote that users love their new Android
phones.`.replace(/\n/g, ' ');
const LINE = '-'.repeat(60);
const BODY = {content: TEXT, type: 'PLAIN_TEXT'};

// Create API clients/endpoints
const NL = new LanguageClient.LanguageServiceClient();
const TL = new Translate();

/** Detect text sentiment */
async function sentAnalysis() {
  const [result] = await NL.analyzeSentiment({document: BODY});
  const sent = result.documentSentiment;
  console.log(`\nSENTIMENT: score (${sent.score.toFixed(2)}), magnitude (${sent.magnitude.toFixed(2)})`);
  console.log(LINE);
}

/** Categorize text */
async function categorizeText() {
  console.log('\nCATEGORIES:');
  const [result] = await NL.classifyText({document: BODY});
  const categories = result.categories;
  for (let cat of categories) {
      console.log(`* ${cat.name.slice(1)} (${cat.confidence.toFixed(2)})`);
  };
  console.log(LINE);
}

/** Translate text to Spanish */
async function translateText() {
  const TARGET = 'es';
  const [txlns] = await TL.translate(TEXT, TARGET);
  let txln = Array.isArray(txlns) ? txlns[0] : txlns;
  console.log(`\nTRANSLATION to "${TARGET}":\n${txln}`);
}

// Display text to process
console.log('TEXT:');
console.log(TEXT);
console.log(LINE);

// Execute all
sentAnalysis()
  .then(categorizeText)
  .then(translateText)
  .catch(console.error);
