# docker-demo
Topic: Containers, Docker and Cloud Computing Demonstration

This repository hosts sample python server code and tooling to demonstrated Docker containers and it's working

It is part of the Webinar session conducted for the same topic.

## Pre-requisite
- Docker installed on your machine.
  Verify with following command
  ```
  docker version
  ```
- Docker id created and logged in from command line.
  Visit `hub.docker.com` to create new docker id. Once login id created; login with following command on terminal (it will prompt for docker id & password)
  ```
  docker login
  ```

## Build & push docker image to docker hub
```
docker build -t kekandotnet/pyserver:0.1 .
docker push kekandotnet/pyserver:0.
```

## Add new tag to existing image
```
docker tag kekandotnet/pyserver:0.1 kekandotnet/docker-demo:0.1
```
OR
```
docker -t kekandotnet/docker-demo:0.1 -t kekandotnet/docker-demo-1:0.1
```

## List local docker images
```
docker images
```
## Remove local image
```
docker rmi kekandotnet/pyserver:0.1
```
OR
```
docker rmi -f kekandotnet/pyserver:0.1
```
## Download image from docker registry
```
docker pull kekandotnet/docker-demo:0.1
```

## Run docker
```
docker run -d -p 8080:80 kekandotnet/docker-demo:0.1
```

## Check running dockers
```
docker ps
docker ps -a
```

## Stop and remove docker container
```
docker stop kekandotnet/docker-demo:0.1
docker rm kekandotnet/docker-demo:0.1
```
OR
```
docker rm -f kekandotnet/docker-demo:0.1
```

## License
Apache 2.0

## Author
- Kedar Kekan (mailbox.kedar@gmail.com)