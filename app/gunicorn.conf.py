import os


bind = "0.0.0.0:8080"
workers = int(os.environ.get("WEB_CONCURRENCY", 2)) # Permite configurar por variável de ambiente
timeout = int(os.environ.get("GUNICORN_TIMEOUT", 10))
worker_class = "gthread"
max_requests = int(os.environ.get("MAX_REQUESTS", 5000))