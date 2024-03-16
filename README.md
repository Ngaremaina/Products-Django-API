# Django API CRUD

This project is a Django API that implements CRUD (Create, Read, Update, Delete) functionality for managing products.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Introduction

This Django API provides endpoints to perform CRUD operations on products. It is designed to be easily integrated into Django projects requiring a RESTful API backend.

## Features

- Create, Read, Update, and Delete operations for managing products.
- RESTful API design for easy integration with frontend applications.
- Django ORM for database operations.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Python (>=3.6)
- Django

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/Ngaremaina/Products-Django-API
    ```

2. Navigate to the project directory:

    ```
    cd Products-Django-API
    ```
3. Install and activate a virtual environment:
    ```
    python -m virtualenv env
    source env/bin/activate
    ```

4. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Apply database migrations:

    ```
    python manage.py migrate
    ```

6. Run the development server:

    ```
    python manage.py runserver
    ```

## Usage

To use the API, you can make requests to the defined endpoints using tools like `curl`, Postman, or integrate it into your frontend application.

## API Endpoints

### Products
- `GET http://127.0.0.1:8000/products/`: Retrieve all products.
- `GET http://127.0.0.1:8000/products/<id>/`: Retrieve a specific product.
- `POST http://127.0.0.1:8000/products/`: Create a new product and its variants.
- `PUT http://127.0.0.1:8000/products/<id>/`: Update a specific product.
- `DELETE http://127.0.0.1:8000/products/<id>/`: Delete a specific product.

### Variants
- `GET http://127.0.0.1:8000/variants/`: Retrieve all variants.
- `GET http://127.0.0.1:8000/variants/<id>/`: Retrieve a specific variant.
- `POST http://127.0.0.1:8000/variants/`: Create a new variant for a specific product.
- `PUT http://127.0.0.1:8000/variants/<id>/`: Update a specific variant for a specific product.
- `DELETE http://127.0.0.1:8000/variants/<id>/`: Delete a specific variant.

## License

This project is licensed under the [Apache License](LICENSE).

