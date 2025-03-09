# Bible Stories
Bible stories is an idea, based on ``black stories``. 
This is a simple Flask application that can be run in a Docker container.

## Prerequisites

You need to have Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).

## Building the Docker Image

To build the Docker image, navigate to the project root directory (where the Dockerfile is located) in your terminal and run the following command:

```bash
sudo docker build -t bible-stories .
```

## Deploy

```bash
sudo docker run -p 4000:80 bible-stories
```

This will start the Docker container and map port 80 in the container to port 4000 on your host machine.