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
// FILE:    maps_geocode.js
// POST:    dev.to/wescpy/explore-the-world-with-google-maps-apis-lhj

require('dotenv').config();
const { Client } = require("@googlemaps/google-maps-services-js");

const ADDRESS = '1600 Amphitheatre Pkwy 94043';
const GMAPS = new Client();
const args = {
  params: {
    key: process.env.API_KEY,
    address: ADDRESS,
  }
};

async function main() {
  const rsp = await GMAPS.geocode(args);
  const res = rsp.data.results[0];
  const geo = res.geometry.location;
  console.log(`** Geocode for "${ADDRESS}": (${geo.lat}, ${geo.lng})`);
}

main().catch(console.error);
