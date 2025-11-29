# Copyright 2025 CyberWeb Consulting LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# FILE:    main.py
# POST:    bit.ly/3Kqv78c and bit.ly/TBD

from base64 import b64encode
import io

from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import mistune

from google import genai
from settings import API_KEY    # can also use .env & python-dotenv

ALLOW_EXTS = {'png', 'jpg', 'jpeg', 'gif'}  # allowed types
MODEL_NAME = 'gemini-2.5-flash'         # Gemini LLM model
THUMB_DIMS = 480, 360                   # thumbnail dimensions
JINUN_TMPL = 'index.html'               # Jinja2/Nunjucks template

app = FastAPI()                         # FastAPI application
templates = Jinja2Templates(directory='templates')
GENAI = genai.Client(api_key=API_KEY)   # API key authz

def is_allowed_file(fname: str) -> bool:
    'check if file (name extension) an allowed file type'
    return '.' in fname and fname.rsplit('.', 1)[1].lower() in ALLOW_EXTS


@app.post('/')
async def process_form(request: Request,
                  file: UploadFile = File(...),
                  prompt: str = Form(...)):
    'application POST handler processes file upload & prompt'

    # initialize template context with upload URL (& required request)
    context: dict = {'upload_url': '/', 'request': request}

    # no attached file
    if not file.file:
        context['error'] = 'No uploaded file'
        return templates.TemplateResponse(JINUN_TMPL, context)

    # reject unacceptable uploads
    fname = file.filename.strip()
    if not fname:
        context['error'] = 'Upload must have file name'
        return templates.TemplateResponse(JINUN_TMPL, context)
    if not is_allowed_file(fname):
        context['error'] = 'Only JPG/PNG/GIF files allowed'
        return templates.TemplateResponse(JINUN_TMPL, context)

    # require genAI prompt
    if not prompt:
        context['error'] = 'LLM prompt missing'
        return templates.TemplateResponse(JINUN_TMPL, context)

    # process image and create its thumbnail
    try:
        image = Image.open(file.file)  # open image with PILlow
        thumb = image.copy()        # copy to make thumb
        thumb.thumbnail(THUMB_DIMS) # resize thumb for display
        img_io = io.BytesIO()       # create IO obj for thumb
        thumb.save(img_io, format=image.format) # save thumb to IO obj
        img_io.seek(0)              # "back to the top" of IO obj

    # handle issues with PILlow or io.BytesIO
    except IOError:

        context['error'] = 'Invalid image file/format'
        return templates.TemplateResponse(JINUN_TMPL, context)

    # render model, prompt, base64-encoded thumb, result
    context['model']  = MODEL_NAME
    context['prompt'] = prompt
    thumb_b64 = b64encode(img_io.getvalue()).decode('ascii')
    context['image']  = f'data:{file.content_type};base64,{thumb_b64}'
    context['result'] = mistune.html(GENAI.models.generate_content(
            model=MODEL_NAME, contents=(prompt, image)).text)

    # show processed results (POST)
    return templates.TemplateResponse(JINUN_TMPL, context)


@app.get('/')
async def display_form(request: Request):
    'application GET handler displays empty form'
    # set template context with required values & show form
    context: dict = {'upload_url': '/', 'request': request}
    return templates.TemplateResponse(JINUN_TMPL, context)


if __name__ == '__main__':
    import os
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', reload=True,
                port=int(os.environ.get('PORT', 8080)))
