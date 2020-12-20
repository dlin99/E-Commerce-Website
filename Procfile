web: gunicorn ecommerce.wsgi
worker: celery -A ecommerce.tasks worker --loglevel=info --concurrency=1