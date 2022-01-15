import os
from flask import Flask


from applications.extensions import init_plugs
from applications.view import init_view
from applications.configs import config


def create_app(config_name=None):
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    if not config_name:
        # try to read from the local environment
        config_name = os.getenv('FLASK_CONFIG', 'development')

    # configuration
    app.config.from_object(config[config_name])
    
    # plugins
    init_plugs(app)

    # route
    init_view(app)

    return app

