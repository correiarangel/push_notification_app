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

# Atribuindo a aplicação à variável 'app'
app = create_app()

if __name__ == '__main__':
    # Iniciar o servidor Flask em modo debug
    app.run(host='0.0.0.0', port=8080, debug=True)


