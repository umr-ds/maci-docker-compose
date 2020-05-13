FROM ubuntu:20.04

ARG COREVERSION=6.4.0
ARG CONTRELEASE=1

LABEL maintainer="msommer@informatik.uni-marburg.de"
LABEL name="maciresearch/core_worker"
LABEL url="https://github.com/umr-ds/maci-docker-compose"
LABEL version="${COREVERSION}-${CONTRELEASE}"

ENV DEBIAN_FRONTEND noninteractive

# update system
RUN apt update && apt dist-upgrade -y && apt clean

# install wget so that we can download the CORE package
RUN apt update && apt install -y wget && apt clean

# install CORE
RUN wget --quiet https://github.com/coreemu/core/releases/download/release-$COREVERSION/core_${COREVERSION}_amd64.deb \
    && apt install -y ./core_${COREVERSION}_amd64.deb \
    && apt clean \
    && rm core_${COREVERSION}_amd64.deb

# the CORE package installs the library to /usr/local/lib/python3.6/dist-packages
# Ubuntu 20.04 ships with Python 3.8 however, so that path is not sreachred by default
# For this reason we symlink it to the mor generel /usr/lib/python3/dist-packages
RUN ln -s /usr/local/lib/python3.6/dist-packages/core /usr/lib/python3/dist-packages/ \
    && ln -s /usr/local/lib/python3.6/dist-packages/core-${COREVERSION}-py3.6.egg-info /usr/lib/python3/dist-packages/

# install CORE dependencies which the CORE-package fails to declare
RUN apt update \
    && apt install -y \
    python3-netaddr \
    python3-grpcio \
    python3-protobuf \
    python3-fabric \
    python3-decorator \
    python3-lxml \
    python3-pyproj \
    python3-mako \
    python3-distutils \
    && apt clean

# MACI dependencies
RUN apt update \
    && apt install -y iperf \
    && apt clean

# install ssh deamon
RUN apt update \
    && apt install -y ssh \
    && apt clean
RUN mkdir /run/sshd
COPY id_ed25519.pub /root/.ssh/authorized_keys
EXPOSE 22

# development tools
RUN apt update \
    && apt install -y \
    iputils-ping \
    net-tools \
    vim \
    neovim \
    nano \
    && apt clean

ENV IDLE=-1

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
