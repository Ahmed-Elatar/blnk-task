# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY . .



RUN apt-get update \
    && apt-get install -y \
        gcc \
        libpq-dev \
        # redis-server \
    && rm -rf /var/lib/apt/lists/*
    



RUN pip install -r requirements.txt


# RUN service redis-server start
#   RUN /etc/init.d/redis-server restart
# RUN celery -A pro worker -l info


COPY pro /app


EXPOSE 8000


CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000"]
