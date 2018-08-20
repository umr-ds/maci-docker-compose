FROM ubuntu:16.04

ENV BACKEND=maci-backend
ENV IDLE=-1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    automake \
    autoconf \
    build-essential \
    libtool \
    software-properties-common \
    iputils-ping \
    vim \
    iperf \
    wget \
    ca-certificates \
    bridge-utils \
    ebtables \
    kmod \
    iproute2 \
    libxml2-dev \
    pkg-config \
    libprotobuf-dev \
    protobuf-compiler \
    libpcap-dev \
    libpcre3-dev \
    uuid-dev \
    debhelper \
    quagga \
    libev4 \
	python \
    python-enum34 \
    python-lxml \
    python-pyroute2 \
    python-psutil \
    python-protobuf \
    python-setuptools \
    python-zmq \
  	python-monotonic \
  	python-subprocess32 \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/coreemu/core/releases/download/release-5.1/python-core_systemd_5.1_all.deb \
    && dpkg -i python-core_systemd_5.1_all.deb \
    && rm python-core_systemd_5.1_all.deb

RUN cd /root/ \
    && wget https://github.com/adjacentlink/emane/archive/v1.2.1.tar.gz \
    && tar -xvf v1.2.1.tar.gz \
    && cd emane-1.2.1 \
    && ./autogen.sh \
    && ./configure \
    && make deb WITHOUT_PYTHON3=1 -j4 \
    && cd .debbuild \
    && dpkg -i *.deb

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
