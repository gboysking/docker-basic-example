# Sharing Volumes Between Applications with Docker Compose

This repository provides an example of how to share log files between two Python applications using Docker Compose. Through this example, you can learn how to define and use volumes in Docker Compose.

[https://tobelinuxer.tistory.com/87]

## Components

This example includes the following components:

- Two Python applications (app1 and app2)
- Python 3.9 (base image)
- Docker Compose file (docker-compose.yml)

## Usage

To run this example, you need Docker and Docker Compose. Follow the instructions below to run the example:

1. Build the applications.

```
docker-compose build
```

2. Run the applications.

```
docker-compose up
```

You can now access the log files on the host machine by running the following commands:

```
# Get the path to the log file on the host machine
docker volume inspect {project_name}_logs | grep Mountpoint | awk '{print $2}' | sed 's/.$//' | awk '{print $1 "/app.log"}' | xargs tail -f

```

Replace `project_name` with the name of your project (by default it's the name of the parent directory where the `docker-compose.yml` file is located).

## Notes

- This example is not intended to demonstrate how to build a full web application. Instead, it is a simple example of how to share log files between two Python applications using Docker Compose.

## References

- [Docker Docs - Docker Compose](https://docs.docker.com/compose/)
- [Docker Docs - Manage data in Docker](https://docs.docker.com/storage/)