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
// FILE:    md2docs.js
// POST:    dev.to/wescpy/TBD

const fs = require('fs').promises;
const path = require('path');
const process = require('process');
const { authenticate } = require('@google-cloud/local-auth');
const { google } = require('googleapis');

const FILENAME = 'quickbrownfox.md';  // change to your own Markdown file
const CREDENTIALS_PATH = path.join(process.cwd(), 'client_secret.json');
const TOKEN_STORE_PATH = path.join(process.cwd(), 'storage.json');
const SCOPES = [ 'https://www.googleapis.com/auth/documents' ];

/**
 * Load any saved credentials or null
 *
 * @return {(Promise<JSONClient|null>)}
 */
async function loadSavedCredentialsIfExist() {
  try {
    const content = await fs.readFile(TOKEN_STORE_PATH);
    const credentials = JSON.parse(content);
    return google.auth.fromJSON(credentials);
  } catch (err) {
    return null;
  }
}

/**
 * Save credentials
 *
 * @param {JSONClient} `client` credentials
 * @return {Promise<void>}
 */
async function saveCredentials(client) {
  const content = await fs.readFile(CREDENTIALS_PATH);
  const keys = JSON.parse(content);
  const key = keys.installed || keys.web;
  const payload = JSON.stringify({
    type: 'authorized_user',
    client_id: key.client_id,
    client_secret: key.client_secret,
    refresh_token: client.credentials.refresh_token,
    access_token: client.credentials.access_token,
    token_expiry: client.credentials.token_expiry,
    scopes: client.credentials.scopes,
  });
  await fs.writeFile(TOKEN_STORE_PATH, payload);
}

/**
 * Authorize user credentials, authenticating user first if necessary
 *
 * @return {JSONClient} client credentials
 */
async function authorize() {
  var client = await loadSavedCredentialsIfExist();
  if (client) return client;
  client = await authenticate({
    scopes: SCOPES,
    keyfilePath: CREDENTIALS_PATH,
  });
  if (client.credentials) await saveCredentials(client);
  return client;
}


/**
 * Parse Markdown, strip to plain text, create styling actions
 *
 * @param {String} `fname` Filename of Markdown content
 * @return {Promise<Array[String, Array]>} `[content, actions]` Text to write & styling actions
 */
async function read_parse_md(fname) {
  // read Markdown content
  var contentBuf = await fs.readFile(FILENAME);
  var content = await contentBuf.toString('utf-8');
  //console.log(content);

  // parse actions & remove tokens; convert to plain text
  var actions = [];  // Markdown styling actions
  const matches = await content.matchAll(/(([_*])([^\2]+)\2)/g);
  for (const match of matches) {
      const [ md, dl, pt ] = await match.slice(1, 4); // MD str, delimiter, plain text str
      var i = await content.indexOf(md);    // begin index for styling
      var j = i + pt.length + 1;     // end index for styling
      content = await content.replace(md, pt);   // replace MD with plain text
      var action = (dl == '*') ? 'bold' : 'italic';  // Markdown action
      await actions.push([ action, i, j ]);      // add to styling actions
  }
  //console.log([actions]);
  return [ content, actions ];
}


/**
 * Create new & empty Google Doc and return file ID
 *
 * @param {google.docs} `DOCS` Google Docs API client/service endpoint
 * @param {String} `fname` Filename of Google Doc to create
 * @return {Promise<String>} `rsp.data.documentId` File ID of newly-created Google Doc
 */
async function create_doc(DOCS, fname) {
  // build create request payload, send to Docs API, and return new file ID
  const rsp = await DOCS.documents.create({ requestBody: { title: fname } });
  return rsp.data.documentId;
}


/**
 * Write text into Google Doc
 *
 * @param {google.docs} `DOCS` Google Docs API client/service endpoint
 * @param {String} `text` Text string to write into Google Doc
 * @param {String} `docs_id` File ID of Google Doc to write into
 * @return {Promise<void>}
 */
async function write_text(DOCS, text, docs_id) {
  // build insert request payload & send to Docs API
  const requests = [ { insertText: { location: { index: 1 }, text: text } } ];
  await DOCS.documents.batchUpdate({
    requestBody: { requests: requests },
    documentId: docs_id
  });
}


/**
 * Format text with requested Markdown styling
 *
 * @param {google.docs} `DOCS` Google Docs API client/service endpoint
 * @param {Array} `actions` Filename of Google Doc to create
 * @param {String} `docs_id` File ID of Google Doc to format
 * @return {Promise<void>}
 */
async function format_text(DOCS, actions, docs_id) {
  // build requests payload based on actions Array
  const requests = [];
  for (const [ style, i, j ] of actions) {
    requests.push({
      updateTextStyle: {
        range: { startIndex: i, endIndex: j },
        textStyle: { [ style ]: true }, fields: style
      }
    });
  }

  // send requests to Docs API
  await DOCS.documents.batchUpdate({
      requestBody: { requests: requests },
      documentId: docs_id
  });
}


/**
 * Main application driver
 *
 * @param {JSONClient} `authClient` client credentials
 * @return {Promise<void>}
 */
async function md2docs(authClient) {
    const DOCS = google.docs({ version: 'v1', auth: authClient });
    const [ text, actions ] = await read_parse_md(FILENAME);
    console.log(`** Parsed Markdown file '${FILENAME}' & style actions`);
    const docs_fn = await FILENAME.replace('.md', '');  // remove MD file ext
    const docs_id = await create_doc(DOCS, docs_fn);
    console.log(`** Created '${docs_fn}' (ID: ${docs_id})`);
    await write_text(DOCS, text, docs_id);
    console.log(`** Inserted '${text.replace(/\n/g, "\\n")}' into document`);
    await format_text(DOCS, actions, docs_id);
    console.log('** Completed Markdown formatting in document:', actions);
}

authorize().then(md2docs).catch(console.error);
