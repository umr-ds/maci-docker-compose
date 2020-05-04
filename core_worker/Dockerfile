FROM ubuntu:18.04
LABEL maintainer="msommer@informatik.uni-marburg.de"
LABEL name="maciresearch/core_worker"
LABEL version="6.2.0-1"

ENV DEBIAN_FRONTEND noninteractive

# update system

RUN apt update && apt dist-upgrade

# CORE dependencies
RUN apt update \
    && apt install -y \
    wget \
    bridge-utils \
    ebtables \
    kmod \
    iproute2 \
    libev4 \
    build-essential \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    python3-wheel \
    python3-future \
    python3-tk \
    python3-netaddr \
    python3-mako \
    quagga \
    tcl \
    tk \
    libtk-img \
    lxterminal \
    ethtool \
    psmisc \
    && apt clean

RUN pip3 install grpcio

RUN pip3 install \
    protobuf \
    lxml \
    fabric \
    pyproj

# CORE
RUN wget --quiet https://github.com/coreemu/core/releases/download/release-6.2.0/core_6.2.0_amd64.deb \
    && dpkg -i core_6.2.0_amd64.deb \
    && rm core_6.2.0_amd64.deb

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
    && apt-get clean

ENV IDLE=-1

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
