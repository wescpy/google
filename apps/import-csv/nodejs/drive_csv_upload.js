// Copyright 2024 CyberWeb Consulting LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// Obtain a copy of the License at: apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// FILE:    drive_csv_upload.js
// POST:    dev.to/wescpy/...

const fs = require('fs').promises;
const path = require('path');
const process = require('process');
const {Readable} =  require('stream');
const {authenticate} = require('@google-cloud/local-auth');
const {google} = require('googleapis');

const CREDENTIALS_PATH = path.join(process.cwd(), 'client_secret.json');
const TOKEN_STORE_PATH = path.join(process.cwd(), 'storage.json');
const SCOPES = ['https://www.googleapis.com/auth/drive.file'];
const FILENAME = 'inventory.csv';
const METADATA = {name: FILENAME};


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
 * @param {JSONClient} client credentials
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
 * Upload CSV file as-is with Drive API
 *
 * @param {JSONClient} authClient (client credentials)
 */
async function uploadCSV(authClient) {
  const drive = google.drive({version: 'v3', auth: authClient});
  const data = await fs.readFile(FILENAME);
  const res = await drive.files.create({
    requestBody: METADATA,
    //media: {mimeType: 'text/csv', body: data}
    media: {body: Readable.from(data)}
  });
  console.log(`** Uploaded '${FILENAME}' to Drive (file ID: ${res.data.id})`);
}

authorize().then(uploadCSV).catch(console.error);

/*

$ node drive_csv_upload.js
** Uploaded 'inventory.csv' to Drive (file ID: 1n7xsKTFUeZKaxpB1CbQZl5DfedkxykXq)

$ node drive_csv_upload.js
TypeError: part.body.pipe is not a function
    at multipartUpload (/private/tmp/nodejs1/node_modules/googleapis-common/build/src/apirequest.js:180:27)
    at createAPIRequestAsync (/private/tmp/nodejs1/node_modules/googleapis-common/build/src/apirequest.js:219:17)
    at createAPIRequest (/private/tmp/nodejs1/node_modules/googleapis-common/build/src/apirequest.js:52:16)
    at Resource$Files.create (/private/tmp/nodejs1/node_modules/googleapis/build/src/apis/drive/v3.js:745:65)
    at uploadCSV (/private/tmp/nodejs1/drive_csv_upload.js:98:33)

*/
