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
// FILE:    main.js
// POST:    dev.to/wescpy/gemini-api-102a-putting-together-a-basic-genai-web-app-3e3

require('dotenv').config();
const express = require('express');
const multer = require('multer');
const nunjucks = require('nunjucks');
const sharp = require('sharp');
const { GoogleGenerativeAI } = require("@google/generative-ai");

const PORT = process.env.PORT || 8080;
const ALLOW_EXTS = ['png', 'jpg', 'jpeg', 'gif'];   // allowed types
const MODEL_NAME = 'gemini-1.5-flash';       // Gemini LLM model
const THUMB_DIMS = [480, 360];                      // thumbnail dimensions
const JINUN_TMPL = 'index.html';                    // Jinja2/Nunjucks template

const app = express();                              // Express.js application
app.use(express.urlencoded({ extended: false }));   // querystring parsing
nunjucks.configure('templates', { autoescape: true, express: app });  // templating
const upload = multer({ storage: multer.memoryStorage() }); // file uploads
const genAI = new GoogleGenerativeAI(process.env.API_KEY);  // API key authz
const model = genAI.getGenerativeModel({ model: MODEL_NAME });  // Gemini

// check if file (name extension) an allowed file type
async function is_allowed_file(fname) {
    return (fname.includes('.') && ALLOW_EXTS.includes(
        fname.toLowerCase().slice(((fname.lastIndexOf('.') - 1) >>> 0) + 2)));
}

// main application handler (GET/POST)
app.all('/', upload.single('file'), async (req, rsp) => {
    // initialize template context with upload URL
    let context = {
        upload_url: `${req.protocol}://${req.get('host')}${req.originalUrl}`
    };

    // process image & render results (POST)
    if (req.method === 'POST') {
        // no attached file
        const upload = req.file;
        if (!upload) {
            context.error = 'No uploaded file';
            return rsp.render(JINUN_TMPL, context);
        }

        // reject unacceptable uploads
        const fname = upload.originalname.trim();
        if (!fname) {
            context.error = 'Upload must have file name';
            return rsp.render(JINUN_TMPL, context);
        }
        const allowed = await is_allowed_file(fname);
        if (!allowed) {
            context.error = 'Only JPG/PNG/GIF files allowed';
            return rsp.render(JINUN_TMPL, context);
        }

        // require genAI prompt
        const prompt = req.body.prompt.trim();
        if (!prompt) {
            context.error = 'LLM prompt missing';
            return rsp.render(JINUN_TMPL, context);
        }

        // process image and create its thumbnail
        const image = upload.buffer;            // save image into Buffer
        const mimeType = upload.mimetype;       // image MIME type
        var thumb_b64;                          // base64-encoded thumb
        try {
            const thumb = await sharp(image);   // open img w/Sharp & resize as thumb
            const thumb_buf = await thumb.resize({ width: THUMB_DIMS[0] }).toBuffer();
            thumb_b64 = thumb_buf.toString('base64');
        }
        // handle issues with Sharp
        catch (ex) {
            context.error = 'Invalid image file/format';
            return rsp.render(JINUN_TMPL, context);
        }

        // render model, prompt, base64-encoded thumb, result
        context.model = MODEL_NAME;
        context.prompt = prompt;
        context.image = `data:${mimeType};base64,${thumb_b64}`;
        const payload = { inlineData: { data: image.toString('base64'), mimeType } };
        const result = await model.generateContent([prompt, payload]);
        context.result = await result.response.text();
    }
    // show only form (GET) or with processed results (POST)
    return rsp.render(JINUN_TMPL, context);
});

app.listen(PORT, () => console.log(`* Running on port ${PORT}`));
