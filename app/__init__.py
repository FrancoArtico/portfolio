from flask import Flask
import os

from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app