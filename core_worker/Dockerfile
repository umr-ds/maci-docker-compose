FROM ubuntu:20.04

ARG CORE_TAG=release-7.2.0

LABEL maintainer="msommer@informatik.uni-marburg.de"
LABEL name="maciresearch/core_worker"
LABEL url="https://github.com/umr-ds/maci-docker-compose"
LABEL version="${CORE_TAG}-1"

ENV DEBIAN_FRONTEND noninteractive

# update system, install wget and python
RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install -y wget python3-pip \
    && apt-get clean

RUN wget --quiet https://github.com/coreemu/core/archive/${CORE_TAG}.tar.gz \
    && mkdir core \
    && tar xf ${CORE_TAG}.tar.gz \
    && mv /core-${CORE_TAG} /usr/local/share/core

WORKDIR "/usr/local/share/core"

# Install CORE similar to core's tasks.py file
RUN apt-get update \
    && apt-get install -y automake pkg-config gcc libev-dev ebtables iproute2 ethtool tk python3-tk bash \
    && apt-get clean

RUN python3 -m pip install --user grpcio==1.27.2 grpcio-tools==1.27.2

RUN ./bootstrap.sh
RUN ./configure --prefix="/usr/local"
RUN make -j$(nproc)
RUN make install

WORKDIR "/usr/local/share/core/daemon"
RUN python3 -m pip install .

RUN cp scripts/* "/usr/local/bin"
RUN mkdir -p /etc/core
RUN cp data/* /etc/core

# MACI dependencies
RUN apt-get update \
    && apt-get install -y iperf \
    && apt-get clean

# install ssh deamon
RUN apt-get update \
    && apt-get install -y ssh \
    && apt-get clean
RUN mkdir /run/sshd
COPY id_ed25519.pub /root/.ssh/authorized_keys
EXPOSE 22

# development tools
RUN apt-get update \
    && apt-get install -y \
    iputils-ping \
    net-tools \
    vim \
    neovim \
    nano \
    && apt-get clean

ENV IDLE=-1

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
