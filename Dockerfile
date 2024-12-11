# Use uma imagem base Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Instale dependências do sistema necessárias para compilar pacotes Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    libgpg-error-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Copie os arquivos do projeto para o contêiner
COPY . .

# Atualizar pip para a versão mais recente
RUN pip install --upgrade pip

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta (Railway usará a variável de ambiente PORT automaticamente)
EXPOSE 8080

# Define a variável de ambiente da porta
ENV PORT=8080

# Comando para iniciar o servidor
CMD ["python", "app.py"]
