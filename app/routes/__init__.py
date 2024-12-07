# importa e registra todas as rotas no aplicativo Flask
from .notification_routes import notification_bp
from .page_routes import page_bp
from .utility_routes import utility_bp

def initialize_routes(app):
    app.register_blueprint(notification_bp)
    app.register_blueprint(page_bp)
    app.register_blueprint(utility_bp)
