# hotel_system

This repository contains the API endpoints of Hotel systems. This enables users to be authenticated and authorized before searching for hotels nearby.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- Install `pip` if it is not installed yet in your system

-  To install virtual environment, run in your terminal:
```
pip install virtualenv
```
- To create a virtual environment, in the root folder of the cloned app, run:
```
virtualenv -p python3 venv
```
- To activate the virtualenv:
```
source venv/bin/activate
```

- Run the command below to install all the project dependencies:
```
pip install -r requirements.txt
```
- To deactivate the virtualenv:
```
deactivate
```
### Installing
- Clone this repository
> https://github.com/Celoka/hotel_system.git

- Cd into the cloned app, create a virtualenv and activate(see instruction above for steps to create a virtualenv)

- Create a `.env` file, copy the variables in the `.env_sample` in the root directory of the project and set up the configurations according to your system.

- Ensure to makemigrations then migrate by running the following commands sequencially:
```
- python manage.py makemigrations

- python manage.py migrate
```

- To start the application, in the root directory of the project, run:
```
python manage.py runserver
```
- To run test:

```
python manage.py test
```

- Test coverage:
```
coverage run manage.py test
```

- Coverage report:
```
coverage report
```
## Features of the Project
- Registration
- Login
- Upload Passport Photo

## API Documentation
Link to API documentation:
https://documenter.getpostman.com/view/2103043/SWE6Zxrm?version=latest

## Built With
- Python 3
- Postgresql
- Django Rest Framework (API development)
- Postman (API Test tool)
