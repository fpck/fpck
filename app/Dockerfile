FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

MAINTAINER Xinyaun Yao <yao.xinyuan@gmail.com>

# RUN apt-get update && apt-get install -y \
#     pkg-config \
#     g++ \
#     libgraphviz-dev \
#     llvm
RUN apt-get update && apt-get install -y \
    curl \
    bzip2 \
    g++ && \
    rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda install -c magma-cuda90 && \
    /opt/conda/bin/conda clean -ya

ENV PATH /opt/conda/bin:$PATH

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
# Create a working directory

# RUN curl -so ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh \
#  && chmod +x ~/miniconda.sh \
#  && ~/miniconda.sh -b -p /opt/conda \
#  && rm ~/miniconda.sh \
#  && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
#  && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
#  && echo "conda activate base" >> ~/.bashrc
#
WORKDIR /srv
COPY ./requirements.txt /srv/requirements.txt
COPY ./dev-requirements.txt /srv/dev-requirements.txt

RUN pip install -r requirements.txt --no-cache-dir  && \
    pip install -r dev-requirements.txt  --no-cache-dir
COPY ./ /srv
RUN python setup.py develop
