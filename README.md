# Angular with Restangular example for Django developers

This is a simple todo app that demonstrates using the following stack:

- Django
- TastyPie for RESTful interface
- Angular for MVC Javascript front-end framework
- Restangular for interacting with tastypie

Angular traditionally uses ngResource for network communication. This app uses restangular, a [recent project](https://github.com/mgonto/restangular) that adds missing features when consuming RESTful resources.

More details are available in [this talk](http://www.youtube.com/watch?v=eGrpnt2VQ3s).

## Usage

Run the following to get started:

    git clone git@github.com:ailling/angular-tastypie-example.git
    cd angular-tastypie-example
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt


Create / clear some todos:

    ./manage.py create_todos    # create some todos
    ./manage.py clear_todos     # clear created todos

Run the server and visit http://localhost:8000

    ./manage.py runserver
