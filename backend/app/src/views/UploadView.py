import os

from flask import Blueprint
from flask import current_app as app
from flask import flash, request, redirect, url_for
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from ..models.UploadModel import UploadSchema

upload_api = Blueprint('upload_api', __name__)
upload_schema = UploadSchema()

UPLOAD_FOLDER = '/app/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@upload_api.route('/', methods=['GET', 'POST'])
@cross_origin(allow_headers=['Content-Type'])
def upload_file():
    if request.method == 'POST':
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
