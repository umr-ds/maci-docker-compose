FROM ubuntu:18.04
LABEL maintainer="hoechst@mathematik.uni-marburg.de"
LABEL name="maciresearch/core_worker"
LABEL version="git-develop-20200220"

ENV DEBIAN_FRONTEND noninteractive

# CORE dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    wget \
    bridge-utils \
    ebtables \
    kmod \
    iproute2 \
    libev4 \
    python3 \
    python3-setuptools \
    python3-pip \
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
    && apt-get clean

RUN pip3 install \
    grpcio \
    protobuf \
    lxml \
    fabric

# CORE
## build dependencies
RUN apt-get install -y --no-install-recommends \
    git \
    automake \
    pkg-config \
    gcc \
    iproute2 \
    libev-dev \
    ebtables \
    python3-dev

RUN pip3 install grpcio-tools

# clone & build from source
RUN git clone https://github.com/coreemu/core.git \
    && cd core \
    && git checkout develop \
    && ./bootstrap.sh \
    && ./configure \
    && make \
    && make install

# MACI dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-subprocess32 \
    python-monotonic \
    iperf \
    && apt-get clean

# install ssh deamon
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ssh \
    && apt-get clean
RUN mkdir /run/sshd
COPY id_ed25519.pub /root/.ssh/authorized_keys
EXPOSE 22

# development tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    iputils-ping \
    net-tools \
    vim \
    nano \
    && apt-get clean

ENV IDLE=-1

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
