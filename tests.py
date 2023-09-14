import requests

base_url = 'http://127.0.0.1:5000/api/person'

# CREATE a new person
data = {'name': 'John Doe'}
response = requests.post(base_url, json=data)
print(response.json())

# READ details of a person by ID (replace 1 with the actual person ID)
response = requests.get(base_url + '/1')
print(response.json())

# UPDATE details of an existing person by ID (replace 1 with the actual person ID)
data = {'name': 'Updated Name'}
response = requests.put(base_url + '/1', json=data)
print(response.json())

# DELETE a person by ID (replace 1 with the actual person ID)
response = requests.delete(base_url + '/1')
print(response.json())
