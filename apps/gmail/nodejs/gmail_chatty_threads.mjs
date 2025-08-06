// Copyright 2025 CyberWeb Consulting LLC
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
// FILE:    gmail_chatty_threads.mjs
// POST:    https://bit.ly/4ljSH2W

import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { authenticate } from '@google-cloud/local-auth';
import { google } from 'googleapis';

const CREDENTIALS_PATH = path.join(process.cwd(), 'client_secret.json');
const TOKEN_STORE_PATH = path.join(process.cwd(), 'storage.json');
const SCOPES = ['https://www.googleapis.com/auth/gmail.metadata'];


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
 * Scan your threads and individual msgs in each
 *
 * @param {JSONClient} authClient (client credentials)
 */
async function gmailThreads(authClient) {
  const GMAIL = google.gmail({ version: 'v1', auth: authClient });
  var res = await GMAIL.users.threads.list({ userId: 'me' });
  const threads = res.data.threads;
  if (!threads || threads.length === 0) return;

  for (const thread of threads) {
    var res = await GMAIL.users.threads.get({
      userId: 'me',
      id: thread.id,
      format: 'metadata'
    });
    var tdata = res.data;
    var nmsgs = tdata.messages.length;

    if (nmsgs > 2) {    // dump if <3 msgs in thread
      var msg = tdata.messages[0].payload;
      var subject = '';
      for (const header of msg.headers) {
        if (header.name == 'Subject') {
          var subject = header.value;
          break
        }
      }
      if (subject) {  // dump if no Subject line
        console.log(`-${String(nmsgs).padStart(3, ' ')} msgs: ` +
          `${(subject.length < 45) ? subject : (subject.slice(0, 42)+'...')}`);
      }
    }
  }
}

authorize().then(gmailThreads).catch(console.error);
