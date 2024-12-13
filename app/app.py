from flask import Flask
from routes import initialize_routes
from dotenv import load_dotenv
import os
import logging

# Configuração do logger
logging.basicConfig(level=logging.DEBUG)

# Carregar variáveis de ambiente
load_dotenv()

def create_app():
    """Cria e configura a aplicação Flask"""
    app = Flask(__name__, static_folder="static")
    app.secret_key = os.getenv("FLASK_SECRET_KEY")
    initialize_routes(app)
    logging.info("App created successfully!")
    return app

# Instância única para uso pelo Gunicorn
app = create_app()

if __name__ == '__main__':
    # Execução em modo de desenvolvimento
    port = int(os.getenv("PORT", 8090))
    app.run(host='0.0.0.0', port=port, debug=True)

    
    # Obtém a porta do ambiente ou usa a padrão (8080)
  # port = int(os.environ.get('PORT', 8080))
    
    # Inicia o servidor Flask na porta configurada
    #app.run(host='0.0.0.0', port=port, debug=True)

