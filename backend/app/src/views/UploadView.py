from flask import request, Blueprint, g
from flask_cors import cross_origin

from ..auth.Authentication import Auth
from ..functions.responses import custom_response
from ..models.UploadModel import UploadModel, UploadSchema

upload_api = Blueprint('upload_api', __name__)
upload_schema = UploadSchema()


@upload_api.route('/', methods=['POST'])
@Auth.auth_required
def upload_file():
    """
    Receive base 64 encoded image
    """
    """
    Create Blogpost Function
    """
    req_data = request.get_json()
    req_data['owner_id'] = g.user.get('id')
    data, error = upload_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    post = UploadModel(data)
    post.save()
    data = upload_schema.dump(post).data
    return custom_response(data, 201)
