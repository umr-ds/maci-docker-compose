FROM maciresearch/core_worker:0.2

ENV DEBIAN_FRONTEND noninteractive

# CORE dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    tcl \
    tk \
    libtk-img \
    lxterminal \
    && rm -rf /var/lib/apt/lists/*

# CORE gui
RUN wget --no-check-certificate https://github.com/coreemu/core/releases/download/release-5.2/core-gui_5.2_amd64.deb \
    && dpkg -i core-gui_5.2_amd64.deb \
    && rm core-gui_5.2_amd64.deb

# development tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    iputils-ping \
    net-tools \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
