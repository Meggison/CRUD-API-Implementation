# API Documentation

This documentation provides information on how to use the Simple CRUD API for managing persons. The API allows you to perform basic CRUD operations on person resources.

## API Endpoints

### Create a Person

**Endpoint:** `/api/person` (HTTP POST)

**Request Format:**
json
{
  "name": "John Doe"
}
Get a Person
Endpoint: /api/person/{id} (HTTP GET)
{
  "name": "John Doe"
}
Update a Person
Endpoint: /api/person/{id} (HTTP PUT)
{
  "name": "Updated Name"
}

Delete a Person
Endpoint: /api/person/{id} (HTTP DELETE)
{
  "message": "Person deleted successfully"
}


Limitations and Assumptions:
The API assumes that the "name" field is mandatory for creating and updating a person. Missing or empty "name" values will result in errors.
It is assumed that the API is running locally at http://localhost:5000. Adjust the base URL for your specific deployment.

Setting Up and Deploying the API:
Follow these steps to set up and deploy the API:
Clone the repository from GitHub.
Create a virtual environment and activate it (recommended).
Install the required dependencies from the requirements.txt file using pip install -r requirements.txt.
Run the Flask application using python app.py. The API will be accessible at http://localhost:5000.
Use tools like Postman or scripts to interact with the API as shown in the "Sample Usage" section.

