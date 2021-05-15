from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from flask_session import Session
from flask_mail import Mail
from flask_script import Manager
from app.config import DevelopmentConfig, TestConfig, ProductionConfig
import os

db = SQLAlchemy()
mail = Mail()


def create_app():

    app = Flask(__name__)
    config_name = os.environ.get('FLASK_ENV')

    # dev and prod environment
    if config_name == "development":
        from app.views.views import user_page
        app.config.from_object(DevelopmentConfig)
        cors = CORS(app, supports_credentials=True)
        app.register_blueprint(user_page)
        from app.models.user_db import db
        from app.models.crypt_db import db
        from app.models.user_crypt_db import db
        from app.utils.execute_user_db import db
        from app.utils.execute_crypt_db import db
        db.init_app(app)
        Migrate(app, db)
        mail.init_app(app)

        return app

    elif config_name == "production":

        from app.views.views import user_page
        app.config.from_object(ProductionConfig)
        cors = CORS(app, supports_credentials=True)
        app.register_blueprint(user_page)
        from app.models.user_db import db
        from app.models.crypt_db import db
        from app.models.user_crypt_db import db
        from app.utils.execute_user_db import db
        from app.utils.execute_crypt_db import db
        db.init_app(app)
        Migrate(app, db)
        mail.init_app(app)

        return app

    # test environment
    db = SQLAlchemy()
    app.config.from_object(TestConfig)
    from app.views.views import user_page
    app.register_blueprint(user_page)
    db.init_app(app)
    app.app_context().push()
    Migrate(app, db)
    mail.init_app(app)

    # manager = Manager(app)
    # manager.add_command('db', MigrateCommand)

    return app
