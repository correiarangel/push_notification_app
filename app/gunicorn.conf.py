import os
import multiprocessing

bind = "0.0.0.0:8080" # Porta fixa dentro do contêiner
workers = multiprocessing.cpu_count() * 2 + 1
timeout = int(os.environ.get("GUNICORN_TIMEOUT", 60))
worker_class = "gthread"