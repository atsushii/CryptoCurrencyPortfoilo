from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import jinja2
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/*": {"origin": "*"}})
    from app.views.views import user_page
    app.config.from_object(Config)
    app.register_blueprint(user_page)
    app.jinja_env.globals.update(zip=zip)
    from app.models.user_db import db
    from app.models.crypt_db import db
    from app.models.user_crypt_db import db
    from app.utils.execute_user_db import db
    from app.utils.execute_crypt_db import db

    bootstrap = Bootstrap(app)
    db.init_app(app)
    Migrate(app, db)

    return app


app = create_app()
