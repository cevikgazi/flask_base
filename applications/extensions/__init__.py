from flask import Flask

from .init_error_views import init_error_views
from .init_dotenv import init_dotenv


def init_plugs(app: Flask) -> None:

    init_error_views(app)
    init_dotenv()
