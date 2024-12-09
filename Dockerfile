# Use uma imagem base Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta (Railway usará PORT automaticamente)
EXPOSE 8080

# Comando para iniciar o servidor
CMD ["python", "app.py"]
