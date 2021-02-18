# CRM

### Getting Started

Python Version: python 3.8.2 

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).


##### *Setup service on local server*

```bash
# Create project directory
$ mkdir /opt/demo

# Change dir to /opt/sperotel_backend
$ cd /opt/demo

# Create Virtual environment for python 3.8.2 
$ virtualenv venv

# Activate Virtual environment
$ source venv/bin/activate

# Clone Repository
$ 

# Change dir to sperotel_backend
$ cd demo

# Install Requirements
$ pip install -r requirements.txt

# Copy etc/config.yaml to /etc/sperotel/config.yaml
$ cp etc/config.yaml /etc/demo/config.yaml

# Edit value in config.yaml and save changes, if required
$ nano /etc/demo/config.yaml

# Create database
$ Create database sperotel_backend, you can use mysql, postgresql, RDS etc

# Django database Migrate
$ python manage.py migrate

# Django Create Superuser
$ python manage.py createsuperuser

# Django runserver on local server
$ python manage.py runserver
```
