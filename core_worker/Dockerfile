FROM ubuntu:18.04
LABEL maintainer="msommer@informatik.uni-marburg.de"
LABEL name="maciresearch/core_worker"
LABEL version="6.2.0-2"

ENV DEBIAN_FRONTEND noninteractive

# update system
RUN apt update && apt dist-upgrade

# CORE dependencies which can not be installed via the package manager
RUN apt update && apt install -y python3-pip && apt clean

RUN pip3 install grpcio

RUN pip3 install \
    protobuf \
    lxml \
    fabric \
    pyproj

# install wget so that we can download the CORE package
RUN apt update && apt install -y wget && apt clean

# install CORE
RUN wget --quiet https://github.com/coreemu/core/releases/download/release-6.2.0/core_6.2.0_amd64.deb \
    && apt install -y ./core_6.2.0_amd64.deb \
    && apt clean \
    && rm core_6.2.0_amd64.deb

# install CORE dependencies which the CORE-package fails to declare
RUN apt update \
    && apt install -y \
    python3-netaddr \
    python3-mako \
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
