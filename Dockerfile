# Use uma imagem base Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema (para garantir que as dependências Python sejam instaladas corretamente)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta (Railway usará a variável de ambiente PORT automaticamente)
EXPOSE 8080

# Definir variáveis de ambiente, incluindo o PORT
# O Railway automaticamente fornece essas variáveis quando o contêiner é iniciado.
ENV PORT=8080

# Comando para iniciar o servidor
CMD ["python", "app.py"]
