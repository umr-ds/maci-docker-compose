FROM ubuntu:16.04

RUN apt-get update

# General dependencies
RUN apt-get install -y \
  git \
  mercurial \
  wget \
  vim \
  autoconf \
  bzr \
  cvs \
  unrar \
  build-essential \
  clang \
  valgrind \
  gsl-bin \
  libgsl-dev \
  flex \
  bison \
  libfl-dev \
  tcpdump \
  sqlite \
  sqlite3 \
  libsqlite3-dev \
  libxml2 \
  libxml2-dev \
  vtun \
  lxc \
  iperf \
  iproute2 \
  iputils-ping \
  net-tools \
  socat build-essential \
  tcpdump \
  x11-xserver-utils \
  xterm \
  cmake \
  libc6-dev \
  libc6-dev-i386 \
  lsb-release \
  g++-multilib

# Python components
RUN apt-get install -y \
  python \
  python-dev \
  python-monotonic \
  python-setuptools \
  python-minimal \
  python-subprocess32 \
  python-pygraphviz \
  python-kiwi \
  python-gnome2 \
  python-rsvg \
  python-gnome2-desktop-dev \
  python-pygoocanvas

WORKDIR /root

# Fetch NS-3 source
RUN wget http://www.nsnam.org/release/ns-allinone-3.28.tar.bz2
RUN tar -xf ns-allinone-3.28.tar.bz2

# Configure and compile NS-3
RUN cd ns-allinone-3.28 && ./build.py --enable-examples --enable-tests && cd ns-3.28 && ./waf install
ENV LD_LIBRARY_PATH=/usr/local/lib 

# Create working directory
WORKDIR /worker

COPY entrypoint.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["sh", "/entrypoint.sh"]
