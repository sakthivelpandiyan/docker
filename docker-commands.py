#List only the docker container which is running.
docker container ls -q

#List docker container both running and stopped
docker container ls -a

#Stop all the docker container which are running.
docker stop $(docker ps -aq)

#start all the docker container which are stopped.
docker start $(docker ps -aq)

#remove all the docker container in one shot
docker rm $(docker ps -aq)

#remove one or two docker container
docker rm $containerid1 $containerid2

#list the docker container
docker container ls

#run the docker in interactive mode

docker run -it ubuntu

#pull the image from the repo
docker pull  mysql

#pull the image from the repo and execute
docker run -d <<imagename>>

#removing the image from the local repo
docker rmi <<imagename>>

#inspectning the images
docker images inspect <<imagename>> or docker images inspect <<imageid>>

#getting particular value from the json output of image inspect.
docker image inspect -f {{.RootFS.Layers}} <<container-id>>

#getting particular value from the json output of container
docker container inspect -f {{.NetworkSettings.IPAddress}} <<container-id>>

#Lauching a container: just runtime
docker run <imagename>

#Lauch a container and running background
docker run -d <imagename>

#Login in to lauched container 
docker exec -it <<container-id>> /bin/bash

#port forwarding
docker run -d -p <port no on base mechine>:<port no on container side>  nginx

#Building images from the Dockerfile
docker build -t sakthi/vimeditor .<<File Current path>>

#Copy a file from local to docker container
docker cp <<Local Files name> <<container_id/PATH/Filename>> 

#Copy a File from docker container to local contrainer 
docker cp <<container_id/PATH/Filename>> <<Local Files name>

#Create Network on Docker Container
docker network create --subnet=<<subnet>>/<<bit>> <<Network name>>
    //docker network create --subnet=192.168.10.10/24 docnet

#Create a container with specified network, hostname and ipaddress
docker run -d --hostname <<hostname>> --net <<network name>> --ip <<ipaddress>> <<imageid or image name>>
    // docker run -d -p 4444:22 -p 9010:7001 --hostname orahost1 --net docnet --ip 192.168.10.10 oracle/weblogic:12.2.1.3-generic


#Monitoring the docker using curl

curl --unix-socket /var/run/docker.sock http:/containers/<<container-id>>/stats

