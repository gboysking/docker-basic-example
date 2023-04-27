# Dynamic Task Slot Number Configuration in Docker Swarm

This repository provides example code for dynamically configuring task slot numbers in Docker Swarm. This can increase the scalability of your application and adjust imbalances between tasks (container instances).

## Requirements

To run this example code, you need the following requirements:

- Docker
- Docker Compose

## Usage

1. Build the Docker image.

```
$ docker build -t custom-task-slot-image .
```

2. Deploy the Docker Swarm stack.

```
$ docker stack deploy -c docker-compose.yml task-slot-test
```

3. Check the tasks (container instances) running in the stack.

```
$ docker stack ps task-slot-test
```

## Description of Example Code

The example code consists of the following files:

- `app.py`: A Python application that uses task slot numbers and environment variables to log events.
- `Dockerfile`: The Dockerfile used to build the Docker image.
- `docker-compose.yml`: The Docker Compose file used to deploy the stack.

The example code uses task slot numbers and environment variables to dynamically configure the application. This allows for greater scalability and the ability to adjust imbalances between tasks (container instances).