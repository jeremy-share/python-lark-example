FROM python:3.12

RUN mkdir /opt/mini_query_language
WORKDIR /opt/mini_query_language
COPY requirements.in ./

RUN pip install -r requirements.in
