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
// FILE:    drive_csv_import.mjs
// POST:    dev.to/wescpy/...

import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import {Readable} from 'node:stream';
import {authenticate} from '@google-cloud/local-auth';
import {google} from 'googleapis';

const CREDENTIALS_PATH = path.join(process.cwd(), 'client_secret.json');
const TOKEN_STORE_PATH = path.join(process.cwd(), 'storage.json');
const SCOPES = ['https://www.googleapis.com/auth/drive.file'];

// filenames & MIMEtypes
const DST_FILENAME = 'inventory';
const SRC_FILENAME = DST_FILENAME + '.csv';
const SHT_MIMETYPE = 'application/vnd.google-apps.spreadsheet';
const METADATA = {name: SRC_FILENAME, mimeType: SHT_MIMETYPE};


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
async function importCSV(authClient) {
  const drive = google.drive({version: 'v3', auth: authClient});
  const data = await fs.readFile(SRC_FILENAME);
  const res = await drive.files.create({
    requestBody: METADATA,
    media: {body: Readable.from(data)}
  });
  console.log(`** Imported '${SRC_FILENAME}' as Sheets to '${DST_FILENAME}' (file ID: ${res.data.id})`);
}

authorize().then(importCSV).catch(console.error);
