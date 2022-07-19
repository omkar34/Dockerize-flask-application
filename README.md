# Dockerize-flask-application

Run python-flask application in docker container with optimized image

## Run

Clone the repository

```bash
git clone https://github.com/omkar34/Dockerize-flask-application.git
cd Dockerize-flask-app
```

Build docker image
```bash
sudo docker build -t flask-app .
```

Create and Run docker container from image
```bash
sudo docker run -it -d -p 5000:5000 flask-app:latest
```