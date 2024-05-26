# docker/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ../docker/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ../app /app/app
COPY migrations /app/migrations
COPY manage.py /app
COPY wsgi.py /app

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]


