FROM ubuntu:18.04
LABEL maintainer="sterz@mathematik.uni-marburg.de"
LABEL name="maciresearch/empty_worker"
LABEL version="0.1"

ENV DEBIAN_FRONTEND noninteractive

# MACI dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-subprocess32 \
    python-monotonic \
    iperf \
    wget \
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
ENV CAP=empty

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
