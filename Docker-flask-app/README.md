# Building a Multi-Container Application

## Objective
Create a multi-container application that consists of a simple Python Flask web application and a Redis database. The Flask application should use Redis to store and retrieve data.

### Requirements
Flask Web Application:

1. Flask app that has two routes:
/: Displays a welcome message.
/count: Increments and displays a visit count stored in Redis.

2. Redis Database:
Use Redis as a key-value store to keep track of the visit count.
Dockerize Both Services:

3. Create Dockerfiles for both the Flask app and Redis.
Use Docker Compose to manage the multi-container application.