# src/app.py

import os

from flask import Flask, request
from flask_cors import CORS
from redis import Redis

from .config import app_config
from .models import db, bcrypt
from .views.BlogpostView import blogpost_api as blogpost_blueprint
from .views.UploadView import upload_api as files_blueprint
from .views.UserView import user_api as user_blueprint


def create_app(env_name):
    """
    Create app
    """
    # Filesystem
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = 'uploads/'

    # app initialization
    app = Flask(__name__)
    redis = Redis(host='redis', port=6379)

    app.config.from_object(app_config[env_name])
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')
    app.register_blueprint(files_blueprint, url_prefix='/api/v1/upload')

    @app.route("/hits")
    def hello():
        redis.incr('hits')
        return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

    @app.route('/feedback', methods=['POST'])
    def log_feedback():
        with open(UPLOAD_FOLDER+"feedback.txt", "a") as fo:
            fo.write(request.data.decode("utf-8"))
            print(request.data.decode("utf-8"))
            fo.write('\n')
        return 'Got it!'

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your part 2 endpoint is working'

    return app
