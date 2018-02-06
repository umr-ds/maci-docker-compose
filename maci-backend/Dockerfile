FROM microsoft/dotnet:2.0.5-sdk-2.1.4-jessie

#https://github.com/docker-library/buildpack-deps/blob/587934fb063d770d0611e94b57c9dd7a38edf928/jessie/Dockerfile
RUN set -ex; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		autoconf \
		automake \
		bzip2 \
		file \
		make \
		patch \
		xz-utils \
		zlib1g-dev \
		python \
		; \
		rm -rf /var/lib/apt/lists/*

ENV NODE_VERSION 9.5.0

RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    ppc64el) ARCH='ppc64le';; \
    s390x) ARCH='s390x';; \
    arm64) ARCH='arm64';; \
    armhf) ARCH='armv7l';; \
    i386) ARCH='x86';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV YARN_VERSION 1.3.2

RUN set -ex \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && mkdir -p /opt/yarn \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \
  && rm yarn-v$YARN_VERSION.tar.gz

#Add user for Jupyter Notebook Access
RUN useradd --uid 1000 --gid 100 --shell /bin/bash --create-home jovyan &&  usermod -aG root jovyan

#Setup MACI
WORKDIR /maci

COPY MassExecution .

RUN set -ex && cd ./maci_backend  \
	&& npm install --silent \
	&& npm install --silent -g gulp \
	&& gulp clean \
	&& gulp \
	&& dotnet restore 

COPY entrypoint.sh /
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["sh", "/entrypoint.sh"]