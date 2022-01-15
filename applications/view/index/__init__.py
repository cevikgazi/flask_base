from applications.view.index.index import index_bp

from . import index


def register_index_views(app):
    """
    Initialize the blueprint

    """

    app.register_blueprint(index_bp)
