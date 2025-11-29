# Copyright 2024 CyberWeb Consulting LLC
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

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import mistune

from google import genai
from settings import API_KEY    # can also use .env & python-dotenv

ALLOW_EXTS = {'png', 'jpg', 'jpeg', 'gif'}  # allowed types
MODEL_NAME = 'gemini-2.5-flash'         # Gemini LLM model
THUMB_DIMS = 480, 360                   # thumbnail dimensions
JINUN_TMPL = 'index.html'               # Jinja2/Nunjucks template

app = Flask(__name__)                   # Flask application
GENAI = genai.Client(api_key=API_KEY)   # API key authz

def is_allowed_file(fname):
    'check if file (name extension) an allowed file type'
    return '.' in fname and fname.rsplit('.', 1)[1].lower() in ALLOW_EXTS


@app.route('/', methods=['GET', 'POST'])
def main():
    'main application (GET/POST) handler'

    # initialize template context with upload URL
    context = {'upload_url': url_for(request.endpoint)}

    # process image & render results (POST)
    if request.method == 'POST':
        # no attached file
        upload = request.files.get('file')
        if not upload:
            context['error'] = 'No uploaded file'
            return render_template(JINUN_TMPL, **context)

        # reject unacceptable uploads
        fname = secure_filename(upload.filename.strip())
        if not fname:
            context['error'] = 'Upload must have file name'
            return render_template(JINUN_TMPL, **context)
        if not is_allowed_file(fname):
            context['error'] = 'Only JPG/PNG/GIF files allowed'
            return render_template(JINUN_TMPL, **context)

        # require genAI prompt
        prompt = request.form.get('prompt').strip()
        if not prompt:
            context['error'] = 'LLM prompt missing'
            return render_template(JINUN_TMPL, **context)

        # process image and create its thumbnail
        try:
            image = Image.open(upload)  # open image with PILlow
            thumb = image.copy()        # copy to make thumb
            thumb.thumbnail(THUMB_DIMS) # resize thumb for display
            img_io = io.BytesIO()       # create IO obj for thumb
            thumb.save(img_io, format=image.format) # save thumb to IO obj
            img_io.seek(0)              # "back to the top" of IO obj

        # handle issues with PILlow or io.BytesIO
        except IOError:
            context['error'] = 'Invalid image file/format'
            return render_template(JINUN_TMPL, **context)

        # render model, prompt, base64-encoded thumb, result
        context['model']  = MODEL_NAME
        context['prompt'] = prompt
        thumb_b64 = b64encode(img_io.getvalue()).decode('ascii')
        context['image']  = f'data:{upload.mimetype};base64,{thumb_b64}'
        context['result'] = mistune.html(GENAI.models.generate_content(
                model=MODEL_NAME, contents=(prompt, image)).text)

    # show only form (GET) or with processed results (POST)
    return render_template(JINUN_TMPL, **context)


if __name__ == '__main__':
    import os
    app.run(debug=True, threaded=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
