# Dockerfile for a Python App
FROM python:3.8
WORKDIR /server
RUN pip3 install flask requests
COPY . .
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]