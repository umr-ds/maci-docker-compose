FROM ubuntu:18.04

ENV BACKEND=maci-backend
ENV IDLE=-1

# CORE dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    wget \
    bridge-utils \
    ebtables \
    iproute2 \
    libev4 \
    python \
    python-enum34 \
    python3 \
    quagga \
    && rm -rf /var/lib/apt/lists/*

# CORE backend
RUN wget --no-check-certificate https://github.com/coreemu/core/releases/download/release-5.1/python-core_systemd_5.1_all.deb \
    && dpkg -i python-core_systemd_5.1_all.deb \
    && rm python-core_systemd_5.1_all.deb

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
