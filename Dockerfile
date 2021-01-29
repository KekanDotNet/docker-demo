FROM python:3.9.1-slim-buster
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask flask_cors dapr
ENTRYPOINT ["python"]
EXPOSE 8080
CMD ["app.py"]