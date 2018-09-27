FROM ubuntu:18.04

ENV BACKEND=maci-backend
ENV IDLE=-1

# CORE dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    wget \
    bridge-utils \
    ebtables \
    kmod \
    iproute2 \
    libev4 \
    python \
    python-enum34 \
    python-lxml \
    python3 \
    quagga \
    && rm -rf /var/lib/apt/lists/*

# CORE backend
RUN wget --quiet --no-check-certificate https://github.com/coreemu/core/releases/download/release-5.2/python-core_sysv_5.2_all.deb \
    && dpkg -i python-core_sysv_5.2_all.deb \
    && rm python-core_sysv_5.2_all.deb

# MACI dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-subprocess32 \
    python-monotonic \
    iperf \
    && rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
