FROM ubuntu:16.04

ENV BACKEND=maci-backend
ENV IDLE=-1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
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
    vim \
    python \
    python-dev \
    python-setuptools \
    python-monotonic \
    python-subprocess32 \
    python-pip \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install cxxfilt

WORKDIR /root

# Fetch NS-3 source
RUN wget http://www.nsnam.org/release/ns-allinone-3.28.tar.bz2 \
    && tar -xf ns-allinone-3.28.tar.bz2 \
    && cd ns-allinone-3.28 \
    && ./build.py --enable-examples --enable-tests \
    && cd ns-3.28 \
    && ./waf install
    
ENV LD_LIBRARY_PATH=/usr/local/lib 


ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"