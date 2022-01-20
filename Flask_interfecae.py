from flask import Flask, render_template, request

app = Flask(__name__)
from ocr_engine import ocr_engine

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower()in ALLOWED_EXTENSIONS

import os
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads\\')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from flask import render_template


@app.route('/', methods = ['GET', 'POST'])

def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg = 'No file Selected')
    
    file = request.files['file']
    if file.filename =='':
        return render_template('upload.html', msg = 'No file')
    
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config[UPLOAD_FOLDER], file.filename))
        extracted =ocr_engine(file)
        return render_template('upload.html', msg = 'OCR completed', extracted= extracted, img_src = UPLOAD_FOLDER + file.filename)
    else:
        return render_template('upload.html')

if __name__ == '__main__':
        app.run()
