import os
from flask import Flask
from flask_bootstrap import Bootstrap
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
"""

bootstrap = Bootstrap()
# migrate = Migrate()
# db = SQLAlchemy()
# lm = LoginManager()
# lm.login_view = 'main.login'


def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)

    # import configuration
    cfg = os.path.join(os.getcwd(), 'config', 'development.py')
    app.config.from_pyfile(cfg)

    # initialize extensions
    bootstrap.init_app(app)
    # db.init_app(app)
    # lm.init_app(app)

    # import blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
