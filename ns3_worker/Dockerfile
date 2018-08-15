FROM ubuntu:16.04

RUN apt-get update

# General dependencies
RUN apt-get install -y \
  gcc \
  g++ \
  mercurial \
  git \
  gsl-bin \
  libgsl2 \
  libgsl-dev \
  flex \
  bison \
  libfl-dev \
  tcpdump \
  sqlite \
  sqlite3 \
  libsqlite3-dev \
  cmake \
  libc6-dev \
  libc6-dev-i386 \
  wget \
  vim

# Python components
RUN apt-get install -y \
  python \
  python-dev \
  python-setuptools \
  python-monotonic \
  python-subprocess32 \
  python-pip \
  build-essential 

RUN pip install cxxfilt

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
