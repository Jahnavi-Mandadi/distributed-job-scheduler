from flask import Flask
from flask_cors import CORS
from app.extensions import db
import os

def create_app():
    app=Flask(__name__)

    CORS(app)

    db_url=(
        f"postgresql://{os.getenv('DATABASE_USER')}:"
        f"{os.getenv('DATABASE_PASSWORD')}@"
        f"{os.getenv('DATABASE_HOST')}:"
        f"{os.getenv('DATABASE_PORT')}/"
        f"{os.getenv('DATABASE_NAME')}"
    )

    app.config["SQLALCHEMY_DATABASE_URI"]=db_url

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)


    #register buleprints
    from app.routes.health_routes import health_bp
    from app.routes.dag_routes import dag_bp
    from app.routes.task_routes import task_bp
    from app.routes.execution_routes import execution_bp
    from app.routes.monitoring_routes import monitoring_bp


    app.register_blueprint(health_bp)
    app.register_blueprint(dag_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(execution_bp)
    app.register_blueprint(monitoring_bp)

    return app