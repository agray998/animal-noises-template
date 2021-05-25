# Dockerfile for a Python App
FROM python:3.8
WORKDIR /api
RUN pip3 install flask
COPY . .
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]