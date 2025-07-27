FROM python:3.12

RUN     apt-get update \
    &&  apt-get install -y graphviz \
    &&  apt-get clean \
    &&  rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/app
WORKDIR /opt/app
COPY requirements.in ./

RUN pip install -r requirements.in
