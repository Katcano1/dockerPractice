Instructions for running the Dockerized QuicksStart application:
* Docker compose up -d 
| creates a docker container and runs it in the background
* Docker attach (container name)
| attaches the terminal's input to the container

Instructions for running dockerized RESTFul app:
* docker compose build
* docker compose up
- preferably use Postman to make requests to the server, but can also use cURL
* Methods for Restful api:
- get localhost:5000/jobs 
- get localhost:5000/jobs/status
- post localhost:5000/jobs
- delete localhost:5000/jobs
- delete localhost:5000/jobs/<uuid>
