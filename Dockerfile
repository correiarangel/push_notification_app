# Use a imagem base do Python
FROM python:3.10-slim

# Instalar dependências do sistema, incluindo pacotes adicionais para compilar wheels
RUN apt-get update && apt-get install -y \
    python3-dev \
    libssl-dev \
    libffi-dev \
    zlib1g-dev \
    build-essential \
    gettext \
    pkg-config \
    libcairo2-dev \
    libpango1.0-dev \
    libglib2.0-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    liblcms2-dev \
    libblas-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar o requirements.txt para dentro do contêiner
COPY requirements.txt .

# Atualizar pip
RUN pip install --upgrade pip

# Remover versão exata de python-debian (se necessário)
RUN sed -i '/python-debian==0.1.43/d' requirements.txt

# Instalar dependências manualmente em etapas, para depuração
RUN pip install --no-cache-dir appdirs==1.4.4
RUN pip install --no-cache-dir attrs==21.2.0
RUN pip install --no-cache-dir bcrypt==3.2.0
RUN pip install --no-cache-dir beautifulsoup4==4.10.0
RUN pip install --no-cache-dir beniget==0.4.1
# Continue instalando os pacotes manualmente

# Expor a porta
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python3", "app/app.py"]

