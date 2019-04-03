# src/app.py

from flask import Flask
from flask_cors import CORS
from redis import Redis

from .config import app_config
from .models import db, bcrypt
from .views.BlogpostView import blogpost_api as blogpost_blueprint
# import user_api blueprint
from .views.UserView import user_api as user_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)
    redis = Redis(host='redis', port=6379)

    app.config.from_object(app_config[env_name])

    CORS(app)

    # initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')

    @app.route("/hits")
    def hello():
        redis.incr('hits')
        return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your part 2 endpoint is working'

    return app
