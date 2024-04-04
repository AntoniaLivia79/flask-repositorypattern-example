An example of a Flask API being used to query a Postgress database table (users) and returning a user record as a response.

The purpose of this project is to demonstrate how a repository design pattern can be used to separate concerns across a data access application.

## Usage

### Run locally with docker

Use docker-compose
```
docker-compose up
```

### Example API requests
```
GET localhost:5000/healthcheck 
```
This request should receive a response body of 
```
{"status": "healthy"}
```

```
GET localhost:5000/api/users/Bob
```
This request should receive a response body of 
```
{"username": "Bob", "country": "UK"}
```

Documentation on how the repository design pattern has been implemented in this example is provided in the docs folder.
