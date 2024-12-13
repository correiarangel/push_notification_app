from flask import Flask
from routes import initialize_routes
from dotenv import load_dotenv
import os
import logging

# Configuração do logger use local
#logging.basicConfig(level=logging.DEBUG)

# Carregar variáveis de ambiente
load_dotenv()

def create_app():
    app = Flask(__name__, static_folder="static")
    app.secret_key = os.getenv("FLASK_SECRET_KEY")
    initialize_routes(app)
    logging.info("App created successfully!")
    return app

# A lógica de inicialização do Gunicorn será responsável 
# pela execução, então removemos app.run().
app = create_app()

# Apenas para desenvolvimento, o Gunicorn gerenciará a execução em produção.
try:
    logging.basicConfig(level=logging.DEBUG)
    app = create_app()
    if __name__ == '__main__':
        app.run(port=8080, debug=True)
except Exception as e:
    logging.error(f"Failed to start the app: {str(e)}")
    
    raise
    
    # Obtém a porta do ambiente ou usa a padrão (8080)
  # port = int(os.environ.get('PORT', 8080))
    
    # Inicia o servidor Flask na porta configurada
    #app.run(host='0.0.0.0', port=port, debug=True)

