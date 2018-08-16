# MACI Docker

This repository provides a set of instructions to create _Docker_ containers to start a full working set of the _MACI_ framework published on https://maci-research.net/

The service is launched with _Docker Compose_ initiating and connecting different _Containers_:

- _maci-backend_ running the management framework based on .Net
- _jupyter_ for analyzing experiments
- _*_worker_ to run experiments (multiple instances can be started, however, be aware of side effects when executing parallel network experiments on the same host).

## Getting Started
### Setup Docker
- Linux (Ubuntu 16.06)

   Docker-CE and Docker compose need to be installed, see https://docs.docker.com/compose/install/

```bash
#run as root
apt-get update
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"
apt-get update
apt-get install docker-ce
curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
service docker start
```

- macOS

   Install Docker (e.g., following these [instructions](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac))

- Windows

   Install Docker (e.g., following these [instructions](https://docs.docker.com/docker-for-windows/)).

### Load Submodules

The _MACI_ framework is loaded as a git submodule and needs to be loaded before starting the container:

```bash
git submodule init
git submodule update --remote
```

### Start Backend with a Mininet Worker
The command below starts all required containers. Replace `<WORKER>` with the worker you wish. The MACI WebUI will be available at [http://localhost:63658](http://localhost:63658)

```
docker-compose -f docker-compose.yml -f mininet.yml up
```

### Stop Backend

```
docker-compose -f docker-compose.yml -f mininet.yml down
```



## Configuring Workers

### Bootstraping Methods
 - From DockerHub to circumvent the long build process of the images:

```
docker pull maciresearch/maci-backend
docker pull maciresearch/core_worker
docker pull macireserach/ns3_worker
docker pull maciresearch/mininet_worker
```

 - Build images from Dockerfiles:

```
docker build -t maciresearch/maci-backend maci-backend/
docker build -t maciresearch/mininet_worker mininet_worker/
docker build -t maciresearch/core_worker core_worker/
docker build -t maciresearch/ns3_worker ns3_worker/
```

### Scale Number of local Workers
Run <N> instances of one <WORKER> (core | ns3 | mininet | ...).
```
docker-compose -f docker-compose.yml -f <WORKER>.yml --scale <WORKER>=<N> up
``` 

### Start remote workers
1. Build or pull the Docker images as before.
2. Run a worker and provide the backend address from the worker's perspectiveand idle shutdown time (optional):

```
docker run --rm --privileged  -v /lib/modules:/lib/modules -e BACKEND=<BACKEND_ADDRESS> -e IDLE=3600 -d maciresearch/mininet_worker
```

Note: In addition to the extended privileges the core worker also needs NET_ADMIN linux kernel capabilities and access to the kernel modules:

```
docker run --rm --privileged  -v /lib/modules:/lib/modules -e BACKEND=<BACKEND_ADDRESS> -e IDLE=3600 -d  --cap-add=NET_ADMIN maciresearch/core_worker
```

### Stop the container
... using the id provided after start:

```
docker stop <CONTAINER_ID>
```                                                                                                   

## Contact

 - [Denny Stohr](https://github.com/dstohr/) 
 - [Alexander Frömmgen](https://github.com/AlexanderFroemmgen)
 - [University of Marburg, Distributed Systems](https://github.com/umr-ds)
