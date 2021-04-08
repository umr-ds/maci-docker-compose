FROM ubuntu:20.10

ARG NS3VERSION=3.33

LABEL maintainer="Markus Sommer <msommer@informatik.uni-marburg.de>"
LABEL name="maciresearch/ns3_worker"
LABEL url="https://github.com/umr-ds/maci-docker-compose"
LABEL version="${NS3VERSION}-1"

ENV BACKEND=maci-backend
ENV IDLE=-1

# update base system
RUN apt update && apt dist-upgrade -y && apt clean

# ns3 base-dependencies
RUN apt update \
    && apt install -y \
    build-essential \
    python3 \
    git \
    mercurial \
    && apt clean

# ns3 python api dependencies
RUN apt update \
    && apt install -y \
    python3-dev \
    python3-setuptools \
    python3-pip \
    git \
    pkg-config \ 
    sqlite3 \
    && apt clean

# Netanim animator
RUN apt update \
    && apt install -y \
    qt5-default \ 
    mercurial \
    && apt clean

# ns-3-pyviz visualizer
RUN apt update \
    && apt install -y \
    gir1.2-goocanvas-2.0 \ 
    python3-gi \ 
    python3-gi-cairo \ 
    python3-pygraphviz \ 
    gir1.2-gtk-3.0 \ 
    ipython3 \
    && apt clean

# MPI-based distributed emulation
RUN apt update \
    && apt install -y \
    openmpi-bin \ 
    openmpi-common \
    openmpi-doc \
    libopenmpi-dev \
    && apt clean

# bake build tool
RUN apt update \
    && apt install -y \
    autoconf \
    cvs \
    bzr \
    unrar \
    && apt clean

# Debugging
RUN apt update \
    && apt install -y \
    gdb valgrind \
    && apt clean

# Support for utils/check-style.py code style check program
RUN apt update \
    && apt install -y \
    uncrustify \
    && apt clean

# GNU Scientific Library (GSL) support for more accurate 802.11b WiFi error models
RUN apt update \
    && apt install -y \
    gsl-bin \
    libgsl-dev \
    libgsl25 \
    libgslcblas0 \
    && apt clean

# read pcap packet traces
RUN apt update \
    && apt install -y \
    tcpdump \
    && apt clean

# Database support for statistics framework
RUN apt update \
    && apt install -y \
    sqlite \
    sqlite3 \
    libsqlite3-dev \
    && apt clean

# Xml-based version of the config store
RUN apt update \
    && apt install -y \
    libxml2 \
    libxml2-dev \
    && apt clean

# Support for generating modified python bindings
RUN apt update \
    && apt install -y \
    cmake \
    libc6-dev \
    libc6-dev-i386 \
    libclang-dev \
    llvm-dev \
    automake \
    python3-pip \
    && apt clean
RUN pip3 install cxxfilt

# A GTK-based configuration system
RUN apt update \
    && apt install -y \
    libgtk-3-dev \
    && apt clean

# Support for openflow module
RUN apt update \
    && apt install -y \
    libxml2 \
    libxml2-dev\
    && apt clean

# other stuff which is necessary, I guess
RUN apt update \
    && apt install -y \
    flex \
    bison \
    wget \
    vim \
    && apt clean

WORKDIR /root

# Install NS-3
RUN wget http://www.nsnam.org/release/ns-allinone-${NS3VERSION}.tar.bz2
RUN tar xf ns-allinone-${NS3VERSION}.tar.bz2 
WORKDIR /root/ns-allinone-${NS3VERSION}
RUN ./build.py --enable-examples --enable-tests
WORKDIR /root/ns-allinone-${NS3VERSION}/ns-${NS3VERSION}
RUN ./waf install
    
ENV LD_LIBRARY_PATH=/usr/local/lib 


ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"