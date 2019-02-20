## Getting started

### Install python3
```
brew install python3
```
## Install pip
```
sudo easy_install pip
```
## Create infra-console virtual environment
```
mkdir ~/.virtualenvs
python3 -m venv ~/.virtualenvs/infra-console
```
## Activate infra-console virtual environment
```
source ~/.virtualenvs/infra-console/bin/activate
```
## Install dependencies
```
pip install -r application/requirements.txt
```
### Create main config file
```
cp application/settings.cfg.j2 application/settings.cfg
```
Don't forget to fill in your local environment config values
 
### Run from Python virtual environment

Make sure your Kubernetes config (~/.kube/config) and aws credentials (~/.aws/credentials) files are setup properly so 
you can connect to Kubernetes clusters

#### Run server
```
export FLASK_APP=main.py
export APP_SETTINGS=settings.cfg
export FLASK_ENV=development
cd application
flask run
```
#### Go to [swagger documentation](http://localhost:5000/api/docs/)

### Run from Docker container

You need to get your Kubernetes config and aws credentials into the application container.
Those files will be copied from your application folder to the ~/root directory inside the application container.
So you need to make sure they exist inside your application folder

Create and configure config files
```
touch application/kube-config
touch application/credentials
```

The following lines have to be uncommented in the Dockerfile
```
COPY ./kube-config /root/.kube/config 
COPY ./credentials /root/.aws/credentials
```

#### launch and run the app containers
```
docker-compose -f infrastructure/docker/docker-compose-local.yml up -d  --build
```
#### Go to [swagger documentation](http://localhost:8080/api/docs/)

### Updating requirements.txt

the requirements.txt file has to be updated every time a new dependency is used
```
pip freeze > application/requirements.txt
```
### To stop using a virtual environment
```
deactivate
```

