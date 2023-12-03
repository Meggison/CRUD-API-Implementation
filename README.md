# Simple CRUD API Documentation

## Overview

This documentation details the usage of the Simple CRUD API for managing person entities. The API facilitates basic CRUD (Create, Read, Update, Delete) operations on person resources.

## API Endpoints

### Create a Person
- **Endpoint:** `/api/person` (HTTP POST)
- **Request Format:** JSON

### Get a Person
- **Endpoint:** `/api/person/{id}` (HTTP GET)
- **Request Format:** JSON

### Update a Person
- **Endpoint:** `/api/person/{id}` (HTTP PUT)
- **Request Format:** JSON

### Delete a Person
- **Endpoint:** `/api/person/{id}` (HTTP DELETE)
- **Request Success:** JSON
{ "message": "Person deleted successfully" }

## Limitations and Assumptions

- The "name" field is mandatory for creating and updating a person.
- Missing or empty "name" values will lead to errors.
- The API is assumed to be running locally at `http://localhost:5000`. Adjust the base URL as per your deployment.

## Setting Up and Deploying the API

Follow these steps to set up and deploy the API:

1. Clone the repository from GitHub.
2. Create a virtual environment and activate it (recommended).
3. Install required dependencies: pip install -r requirements.txt
4. Run the Flask application: python app.py
5. 5. The API will be accessible at `http://localhost:5000`.

## Sample Usage

Utilize tools like Postman or custom scripts to interact with the API endpoints as demonstrated above.

