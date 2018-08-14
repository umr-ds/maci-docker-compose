FROM ubuntu:16.04

ENV SCREEN_WIDTH 1280
ENV SCREEN_HEIGHT 800
ENV SCREEN_DEPTH 16
ENV PASSWORD corepsswd
ENV DEBIAN_FRONTEND noninteractive


RUN apt update
RUN apt upgrade -y
RUN apt install -y \
    openbox \
    obconf \
    git \
    x11vnc \
    xvfb \
    wget \
    python \
    unzip \
    bridge-utils \
    ebtables \
    iproute2 \
    iproute2 \
    iproute \
    libev4 \
    libreadline6 \
    libtk-img \
    tk8.5 \
    dirmngr \
    net-tools \
    tcpdump \
    xterm\
    feh \
    tint2 \
    python-numpy \
    logrotate \
    ca-certificates \
    tshark \
    net-tools \
    rox-filer \
    xorp \
    bird \
    openssh-client \
    openssh-server \
    isc-dhcp-server \
    vsftpd \
    apache2 \
    tcpdump \
    radvd \
    at \
    ucarp \
    openvpn \
    ipsec-tools \
    racoon \
    traceroute \
    mgen \
    wireshark-gtk \
    supervisor \
    gcc \
    g++ \
    autoconf \
    automake \
    libtool \
    libxml2-dev \
    libprotobuf-dev \
    python-protobuf \
    libpcap-dev \
    libpcre3-dev \
    uuid-dev \
    debhelper \
    pkg-config \
    build-essential \
    python-setuptools \
    protobuf-compiler \
    git \
    dh-python \
    python-lxml \
    python-enum34 \
    gawk \
    libreadline-dev \
    quagga

# Python components
RUN apt-get install -y \
	python \
  	python-dev \
  	python-setuptools \
  	python-monotonic \
  	python-subprocess32 \
  	python-pip \
  	build-essential

RUN wget https://github.com/coreemu/core/releases/download/release-5.1/python-core_systemd_5.1_all.deb && \
    wget https://github.com/coreemu/core/releases/download/release-5.1/core-gui_5.1_amd64.deb && \
    dpkg -i python-core_systemd_5.1_all.deb && \
    dpkg -i core-gui_5.1_amd64.deb

RUN mkdir -p ~/.vnc

RUN cd /root && git clone https://github.com/kanaka/noVNC.git && \
    cd noVNC/utils && git clone https://github.com/kanaka/websockify websockify

# We have used wireshark-gtk as that has the least dependencies but CORE expects wireshark
RUN ln -s /usr/bin/wireshark-gtk /usr/bin/wireshark

RUN cd /root/noVNC && ln -sf vnc.html index.html

# Really necessary if root?
# RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap
ADD bg/ /root/
ADD ./config/ /root/.config/
ADD etc/supervisor/conf.d /etc/supervisor/conf.d
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Need a patch to get EMANE to compile with GCC >7
ADD patches/gccfix.diff /root/

# Download EMANE v1.0.1 is the latest supprted
RUN cd /root/ && wget https://github.com/adjacentlink/emane/archive/v1.0.1.tar.gz && tar -xvf v1.0.1.tar.gz && \
    cp gccfix.diff emane-1.0.1 && \ 
    cd emane-1.0.1 && patch -p1 <gccfix.diff && \
    ./autogen.sh && ./configure && make deb WITHOUT_PYTHON3=1 && \
    cd .debbuild && \
    dpkg -i *.deb

WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
