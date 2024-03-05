/*
POST:         ...
FILE:         drive_export_doc_pdf.mjs
COPYRIGHT:    (c)2024 CyberWeb Consulting LLC
LICENSE:      apache.org/licenses/LICENSE-2.0
*/

import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import {authenticate} from '@google-cloud/local-auth';
import {google} from 'googleapis';

const CREDENTIALS_PATH = path.join(process.cwd(), 'client_secret.json');
const TOKEN_PATH = path.join(process.cwd(), 'storage.json');
const SCOPES = ['https://www.googleapis.com/auth/drive.readonly'];
const MIMETYPE = 'application/pdf';
const FILENAME = 'Merged form letter';

/**
 * Load any saved credentials or null
 *
 * @return {(Promise<JSONClient|null>)}
 */
async function loadSavedCredentialsIfExist() {
  try {
    const content = await fs.readFile(TOKEN_PATH);
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
  await fs.writeFile(TOKEN_PATH, payload);
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
 * Query for and export/download Google Doc as PDF with Drive API
 *
 * @param {JSONClient} authClient (client credentials)
 */
async function exportDocAsPDF(authClient) {
  const drive = google.drive({version: 'v3', auth: authClient});
  let res = await drive.files.list({
    q: `name="${FILENAME}"`,
    fields: 'files(id)',
    pageSize: 1
  });
  const file = res.data.files[0];
  console.log(`** Downloading '${FILENAME}'`);
  const destPath = path.join(process.cwd(), `${FILENAME}.pdf`);
  const fh = await fs.open(destPath, 'w');
  const dest = fh.createWriteStream();
  res = await drive.files.export({
    fileId: file.id,
    mimeType: MIMETYPE,
  }, {responseType: 'stream'});
  await res.data.pipe(dest);
}

authorize().then(exportDocAsPDF).catch(console.error);
