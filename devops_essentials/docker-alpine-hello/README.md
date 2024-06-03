##Create a Simple Docker Image Locally Based on Alpine##

Background:
Docker allows users to create lightweight and portable containers from custom images. One of the most lightweight base images used in Docker containers is Alpine, a security-oriented, lightweight Linux distribution.

Objective:
Create a Docker image using the Alpine base image. When a container is run using this image, it should print “Hello, World!” to the console.

Resources:
Docker documentation: https://docs.docker.com/
Alpine Docker image details: https://hub.docker.com/_/alpine
Instructions:
Setup:

Ensure Docker is installed on your machine.
Create a new directory for this project: mkdir docker-alpine-hello && cd docker-alpine-hello
Dockerfile:

In the project directory, create a file named Dockerfile.
Start the Dockerfile by specifying the Alpine base image using the FROM directive.
Use the CMD directive in the Dockerfile to echo “Hello, World!” when the container runs.
Building the Docker Image:

In your terminal or command line, navigate to the directory containing your Dockerfile.
Build the Docker image using the docker build command. Make sure to tag the image for easier reference:
 docker build -t hello-alpine .
Running the Docker Container:

Once the image is built, run a container from the image using the docker run command. If done correctly, you should see “Hello, World!” printed in your console.
 docker run hello-alpine
Notes:

Ensure you’re in the correct directory containing the Dockerfile when building the Docker image.
Double-check the syntax and directives in the Dockerfile to ensure the image builds without errors.
Hints:

The Dockerfile should be minimalistic, making use of the lightweight nature of the Alpine image.
Familiarize yourself with Docker’s CMD and ENTRYPOINT directives to understand which might be better suited for this task.
