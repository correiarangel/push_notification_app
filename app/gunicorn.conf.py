import os
import multiprocessing

bind = "0.0.0.0:" + str(os.environ.get("PORT", 8090))
workers = multiprocessing.cpu_count() * 2 + 1 #numero de workers recomendados
timeout = int(os.environ.get("GUNICORN_TIMEOUT", 60)) #tempo limite configuravel via variavel de ambiente no Railway
worker_class = "gthread" #para economizar memoria