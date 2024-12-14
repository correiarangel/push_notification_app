# Use uma imagem base slim do Python
FROM python:3.10-slim-buster

# Instalar dependências do sistema necessárias para pacotes Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2-dev \
    pkg-config \
    libssl-dev \
    libffi-dev \
    python3-dev \
    zlib1g-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt requirements.txt

# Atualizar pip, setuptools e wheel para evitar problemas de compatibilidade
RUN pip install --upgrade pip setuptools wheel

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Só localç
#COPY .env .

# Copiar o código do aplicativo
COPY app .

COPY app/gunicorn.conf.py /app/gunicorn.conf.py

# Expor a porta padrão (se necessário para Flask ou outro framework)
EXPOSE 8090

# Comando padrão ao iniciar o contêiner
#CMD ["bash"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--worker-class", "gthread", "--max-requests", "5000", "app:app"]


# Comando padrão ao iniciar o contêiner usando Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

#CMD ["sh", "-c", "gunicorn", "--bind", "0.0.0.0:8080 app:app"]

# Comando para rodar a aplicação
#CMD ["python", "app.py"]

# Command to run the application
#CMD ["/env/bin/python", "app.py"]