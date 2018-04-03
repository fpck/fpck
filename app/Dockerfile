FROM python:3.6-slim

MAINTAINER Xinyaun Yao <yao.xinyuan@gmail.com>

# machine learning base library

RUN apt-get update && apt-get install -y \
    pkg-config \
    g++ \
    libgraphviz-dev \
    llvm 

ENV LLVM_CONFIG $(which llvm-config-3.9)
ENV PYTHONPATH "${PYTHONPATH}:/srv"

WORKDIR /srv
COPY ./requirements.txt /srv/requirements.txt
COPY ./dev-requirements.txt /srv/dev-requirements.txt

RUN pip install -r requirements.txt --no-cache-dir  && \
    pip install -r dev-requirements.txt  --no-cache-dir 
