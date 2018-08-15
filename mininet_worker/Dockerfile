FROM buildpack-deps:artful-scm

ENV BACKEND=maci-backend
ENV IDLE=-1

RUN set -ex; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
    iperf \
    iproute2 \
    iputils-ping \
    mininet \
    net-tools \
    socat \
    build-essential \
    openvswitch-testcontroller \
    tcpdump \
    x11-xserver-utils \
    xterm \
    lsb-release \
	python-minimal \
    python-subprocess32 \
    python-monotonic \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /worker

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"