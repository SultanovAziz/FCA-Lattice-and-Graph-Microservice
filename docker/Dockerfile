# docker/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ./docker/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./docker/entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development

ENTRYPOINT ["/app/entrypoint.sh"]
#CMD ["flask", "run", "--host=0.0.0.0", "--reload"]


#in production mode
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app", "--reload"]
