# Load Balancing with Docker Compose

This is an example project demonstrating how to configure and run a load balancing setup using Docker Compose and Nginx.

[https://tobelinuxer.tistory.com/89]

## Prerequisites

- Docker
- Docker Compose

## Usage

1. Run `docker-compose up` to start the load balancer and application services.
2. Open your web browser and go to `http://localhost:8080` to access the application.

## Files

- `docker-compose.yml`: Docker Compose configuration file for defining the services and networks.
- `nginx-proxy.conf`: Nginx configuration file for the load balancer service.
- `nginx-app.conf`: Nginx configuration file for the application service.
- `index-app.html`: Sample HTML file to be served by the application.

## Notes

The application service uses the `sub_filter` module to inject the container's hostname, IP address, and port into the response body. This can be useful for debugging and testing the load balancer setup.