# Bewise test task
Web service project for recieving and saving Questions objects from external 
API service https://jservice.io/.
Uses FastAPI framework, PostgreSQL database and SQLAlchemy ORM.

## Installation
Since this is not a production project, changing database credentials is not required.
It is recommended though to change them in docker-compose.yaml file (lines 16-18) and in app/db.py file (line 5).
Same credentials can be used to access DB with your DB utility (for example PGadmin).

To run service use docker-compose command:

**docker-compose up -d**

Now the web service can be accessed with through your browser with *localhost*. 
To try service (saving and searching processes) use *localhost:8000/docs*.

To turn service off use docker-compose command:

**docker-compose down**

## New Questions

To save Questions click on **POST** section. 
Then click on button **Try it out** and print amount of new Questions that you want to add to your local DB.
Click **Execute** button.

If the operation was successful you will get a response with status code 200.
Response body will contain previous saved Question object (or an empty object if there was none).

## Local DB volumes

Database will save its state on host-machine even if cotainers are restarted or deleted.
This is achieved by using **volumes**.

To check all volumes on your machine use docker command:

**docker volume ls**

To clean database state find volume for this project (original name is "bewise_test_task_postgres_data") ang delete it:

**docker volume rm bewise_postgres_data**



