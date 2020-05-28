# User Profiles REST API

This User Profile API is a Django REST Framework based API that provides basic functionality for managing user profiles information.

## Dependencies:
Python (3.6, 3.7)
Django (3.0.6)

## Getting Started

#### Importing All Requirements
We will importing all the required libraries into our python 
environment that is needed to build and run the api.

1. Create python virtual environmant in vagrant box if doesn't not exist ```mkvirtualenv profiles-rest-api```
2. Activating the python environment if not already activated ```workon profiles-rest-api```
3. Change directories to project folder ```cd {Location to directory}```
4. intall all requiremenets ```pip3 install -r requirements.txt```
  
#### Setting up the Database for the api
By using Django rest framework we are able to setup database based on the 
 model, migrate any changes, run service, and debug while developing.
   1. Make sure that the python env is activate if not then ```workon profiles-rest-api```
   2. Change directories to project folder ```cd {Location to directory}```  
   3. Command for creating DB Migration ```python manage.py makemigrations```
   4. Command for creating DB Migration ```python manage.py migrate```

#### Running Profiles API
Make sure you have the vagrant server running, your ssh into the server, 
have the python env activate, and you are in the correct direct
1. Activate the python virtualenv with command ```workon profiles-rest-api```
2. Change directory to the project folder ```cd {Location to directory}```
3. Make sure that the database configuration is up to date with command ```python manage.py makemigrations```
4. Command for creating DB Migration ```python manage.py migrate```
5. 4. Run Python Django development server to host api ```python manage.py runserver 127.0.0.1:8000```


## Links:
Link for local machine: 

[http://127.0.0.1:8000/users/](http://127.0.0.1:8000/users/ "User Profile API")
[http://127.0.0.1:8000/users/{id}](http://127.0.0.1:8000/users/ "User Profile API Instance")
[http://127.0.0.1:8000/users/?q={username}](http://127.0.0.1:8000/users/ "User Profile API Search")


## Setup Django Admin
Create an initial super user email and named *admin* with a password of your choice.

```python manage.py createsuperuser --email admin@example.com --username admin```
