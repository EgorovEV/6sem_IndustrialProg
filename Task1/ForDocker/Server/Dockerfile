FROM python:3-slim
RUN pip install --upgrade pip
RUN pip install pika
RUN pip install psycopg2

EXPOSE 80
ENV NAME World
CMD ["python", "server.py"]