# MACI Docker

This repository provides a set of instructions to create _Docker_ containers to start a full working set of the _MACI_ framework published on https://maci-research.net/

The service is launched with _Docker Compose_ initiating and connecting three _Containers_:

- _MACI_Backend_ running the management framework based on .Net
- _Jupyter-Notebook_ for analyzing experiments
- _*-Worker_ to run experiments (multiple instances can be started, however, be aware of side effects when executing parallel network experiments on the same host).

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
### Start
The command below starts all required containers. Replace `<WORKER>` with the worker you wish. The CORE worker also offers a GUI at `http://localhost:5900` (not working yet)
```
docker-compose -f docker-compose.yml -f <WORKER>.yml up --build
```

- How do I start up more workers

    Newer Docker-Compose releases support the flag  ```--scale <WORKER>=n``` to launch n workers. 
## Contact

 - [Denny Stohr](https://github.com/dstohr/) 
 - [Alexander Frömmgen](https://github.com/AlexanderFroemmgen)
 - [University of Marburg, Distributed Systems](https://github.com/umr-ds)
