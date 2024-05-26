from flask import Flask
from .extensions import db, migrate, neo4j_driver
from .users.routes import users_bp
from .main.routes import main_bp

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    neo4j_driver.init_app(app)

    # Register Blueprints
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(main_bp, url_prefix='/main')

    return app


