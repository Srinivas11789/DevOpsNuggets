# Deployment with Clusters 
Deployment of an application in a container over a number of machines with replicas to scale the applications as well as recover from failures is the principle concept of cluster deployment.
Such kind of deployment provision requires an automation infrastrucure to create, manage, maintain the clusters. Prominent cluster deployment and tools we will be looking at are,
1. **Docker Swarm**
2. **Kubernetes**

### 1. Docker Swarm
[![N|Solid](https://raw.githubusercontent.com/docker-library/docs/471fa6e4cb58062ccbf91afc111980f9c7004981/swarm/logo.png)](https://nodesource.com/products/nsolid)

A swarm is a group of machines running docker tied togther to form a cluster managed by a swarm manager. Once a cluster is created, all the machines tied together are referred to as nodes/workers. Only the swarm manager machine has authorization to execute commands or add more workers.

  - **Swarm Manager**
  - **Worker or Node**
  
#### Example of a Docker Swarm Deployment
Lets look at a demonstration of a cluster deployment using docker swarm
#### -- Aim:
* To deploy the static webpage in a cluster with multiple instances using docker swarm 
  * **Cluster/Nodes:** Group of virtual machines
  * **Application:** devOps wesite served as static web pages
  * **Tool Used:** Docker swarm

##### Components:
* **Swarm Manager -** Assuming the local machine <machine you are using> to be the manager
* **devOps website as a container -**
  * **Dockerfile -** Using standalone nginx container and serving the static webpages from source 
  * **DockerCompose -** Using a combination of multiple containers of nginx <to host the website> + git-sync <to sync with the repository> + common container storage
  * while in this context, lets take a detour to briefly look at  *dockerFile vs dockerCompose*
    - **dockerFile:**
      * When a self-contained container or monolithic container is to be created which suffices the functionality within itself, a docker file is used 
    - **dockerCompose:**
      * When multiple containers are required which together suffice a functionlity as a team, docker compose is used
* **Virutal machines -** either remote cloud machines or local setup of vms using virutalBox
* **Setup Concern -** Due to cloud machine availability, lets resort to a local setup for the example and peek into an instance of cloud deployment as well.

##### Installation:
* Ensure docker is installed
* Possess any virtual machine setup provision using virtualbox or vmware workstation or make cloud machines setup
##### Setup:
* **TestBed 1:** As per <>, use a nginx container to host the website source code while running docker instance
* **TestBed 2:** Use the dockerCompose file below which uses,
  * *Two containers:*   
    *  nginx - to host the website
    *  git-sync - to sync with the git repo for new changes
  * *Storage* - a common datastore to hold the website source code
```
# A Docker compose to create the application with two containers
# * 1. Nginx container
# * 2. git-sync container
# Reference from: https://hub.docker.com/r/openweb/git-sync/

version: "2"
services:
  nginx:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - website_sources:/usr/share/nginx/html:z
    depends_on:
      - git-sync
    restart: always
  git-sync:
    image: openweb/git-sync:0.0.1
    environment:
      GIT_SYNC_REPO: "https://github.com/gcallah/DevOps"
      GIT_SYNC_DEST: "/git"
      GIT_SYNC_BRANCH: "master"
      GIT_SYNC_REV: "FETCH_HEAD"
      GIT_SYNC_WAIT: "10"
    volumes:
      - website_sources:/git:z
    restart: always
volumes:
  website_sources:
    driver: local
```
##### Steps for Usage:

### References:
* https://docs.docker.com/get-started/part4/#introduction
