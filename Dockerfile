FROM python:2.7-alpine

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools

RUN mkdir /app
ADD requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN rm /app/requirements.txt

COPY riverfordScraper /app/riverfordScraper

WORKDIR /app


CMD ["python", "/app/riverfordScraper/main.py"]