FROM buildpack-deps:artful-scm

ENV BACKEND=maci-backend
ENV IDLE=-1

RUN set -ex; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
	python-minimal python-subprocess32 iperf iproute2   iputils-ping \
    mininet net-tools \
    socat build-essential \
    python-monotonic openvswitch-testcontroller \
    tcpdump \
    x11-xserver-utils \
    xterm \
    lsb-release \
	; \
	rm -rf /var/lib/apt/lists/*

WORKDIR /worker

RUN cp /usr/bin/ovs-testcontroller /usr/bin/ovs-controller
COPY entrypoint.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["sh", "/entrypoint.sh"]
