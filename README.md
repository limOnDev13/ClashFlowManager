# Cash Flow Manager
A test assignment from the IT-Solutions company.

---

## Description
An application for accounting of all monetary transactions 
(test task from IT Solutions). DDS (Cash flow) is the process of accounting, 
managing, and analyzing the receipts and write—offs of funds from a company or 
individual. The application provides the user with the ability to keep records 
of all monetary transactions.

## Setup and launch
To demonstrate how the application works, it is enough to assemble docker containers with 
the ```docker compose up --build``` command. To access the admin area, you will need to go into 
the container terminal with the django application and create a superuser. 
To fill the database, you can upload a fixture /cf_manager/fixture.json. 
If you are using docker compose, you can log into the container terminal 
with the django application (```docker compose exec -ti app /bin/sh```), 
activate the virtual environment (```. .venv/bin/activate```), 
and execute the command (```python ./cf_manager/manage.py loaddata ./cf_manager/fixture.json```).
After that, you can log in to the admin panel with 
**username: admin, password: admin, email: test@test.test**

If the application is running locally via docker (with nginx), 
then the application will work by url. http://127.0.0.1:8000/admin/.

The application implements an API with all the basic CRUD methods. Endpoints:

- ```/cash_flows/api/``` - Methods for working with cash flows
- ```/reference_books/api/statuses/``` - Methods for working with statuses
- ```/reference_books/api/types/``` - Methods for working with types
- ```/reference_books/api/categories/``` - Methods for working with categories
- ```/reference_books/api/subcategories/``` - Methods for working with subcategories

For more information about the API, you can go to the following endpoints:
- ```/api/schema/``` - yml file with openapi specification
- ```/api/schema/swagger/``` - Swagger
- ```/api/schema/redoc``` - Redoc
___

## Technologies
- Django
- DRF
- Postgres
- Docker
- Nginx
