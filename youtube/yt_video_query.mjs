// Copyright 2024 CyberWeb Consulting LLC
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
// FILE:    yt_video_query.mjs
// POST:    dev.to/googleworkspace/getting-started-using-google-apis-api-keys-part-2-38i6
// POST:    dev.to/wescpy/TBD

import 'dotenv/config';
import {google} from 'googleapis';

const QUERY = 'python -snake';
const YOUTUBE = google.youtube({version: 'v3', auth: process.env.API_KEY});

async function listVideos() {
    console.log(`\n** Searching for '${QUERY} videos...`);
    const vids = await YOUTUBE.search.list({part: 'id,snippet', q: QUERY, type: 'video'});
    vids.data.items.forEach(vid => {
        console.log(`http://youtu.be/${vid.id.videoId}\t${vid.snippet.title.substring(0, 48)}`);
    });
}

listVideos().catch(console.error);
