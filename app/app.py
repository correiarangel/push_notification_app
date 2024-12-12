from routes import initialize_routes
from flask import Flask
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def create_app():
    # Define o aplicativo Flask
    app = Flask(__name__, static_folder="static")
    
    # Define a chave secreta para a aplicação
    app.secret_key = os.getenv("FLASK_SECRET_KEY")  

    initialize_routes(app)
    
    return app

if __name__ == '__main__':
    # Cria e executa o aplicativo em modo debug
    app = create_app()
    
    # Obtém a porta do ambiente ou usa a padrão (8080)
    port = int(os.environ.get('PORT', 8080))
    
    # Inicia o servidor Flask na porta configurada
    app.run(host='0.0.0.0', port=port, debug=True)

