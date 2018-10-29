#  Store_Manager_API_Database

Store Manager is a web application that helps store owners manage sales and product inventory records.

## How it Works

- An admin creates a product
- An admin can create an account for a store attendant 
- A store attendant can login with the details provided by the admin
- A logged in user can view available products created by the admin(owner)
- A user chooses on a product and makes an order
- A sale order is made if the product is found and the right quantity is entered
- An admin can update a product
- An admin can also delete a product

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and Setup

Clone the repository below

```
https://github.com/roger254/Store_Manager_API_Database/tree/Develop
```

### Create and activate a virtual environment

    virtualenv env --python=python3.6


if __name__ == '__main__':
    app.run(port=8000)


    source env/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

## Running the application

```bash
$ export FLASK_APP=app.py

$ export FLASK_ENV = development

$ flask run
```

## Endpoints Available

| Method |     Endpoints                   | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   | /api/v1/login/                  | login a user                          | Users         |
| POST   | /api/v1/register/               | register a new user                   | Admin         |
| POST   | /api/v1/product/                | post a new product                    | Admin         |
| POST   | /api/v1/sales/                  | post a new sale                       | Attendant     |
| GET    | /api/v1/product/                | get all products                      | Users         |
| GET    | /api/v1/product/<id>            | get a specific product by id          | Users         |
| GET    | /api/v1/sales/<id>              | get a specific sale by id             | Admin         |
| GET    | /api/v1/sales/                  | get all sale orders                   | Admin         |
| PUT    | /api/v1/product/                | update a product                      | Admin         |
| DELETE | /api/v1/product/                | delete a product                      | Admin         |

### Testing

    nosetests

    - Testing with coverage

    nosetests --with-coverage --cover-package=app

### Author

Roger Brian
