# Get lightweight Alpine Python image
FROM python:3-alpine

# Update Alpine
RUN apk update

WORKDIR /flask

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD ["python", "./main.py"]