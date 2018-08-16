FROM ramonfontes/mininet-wifi:latest

ENV BACKEND=maci-backend
ENV IDLE=-1

RUN	apt-get update; \
    apt-get install -y --no-install-recommends \
    python \
    python-subprocess32 \
    python-monotonic

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /worker
ENTRYPOINT "/entrypoint.sh"
