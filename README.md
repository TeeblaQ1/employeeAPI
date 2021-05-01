# employeeAPI

employeeAPI is a RESTful API built using the django-rest framework that provides services for creating, getting all, getting a specific
employee, updating a specific employee and deleting Employee entities such as represented in the JSON payload defined below:
```JSON
{
    "employees": [
        {
                 "employee_id": "E00001",
                 "first_name": "John",
                 "last_name": "Keynes",
                 "age": 29,
                 "Join_date": "2021-01-15"
         },
         {
                 "employee_id": "E00002",
                 "first_name": "Sarah",
                 "last_name": "Robinson",
                 "age": 54,
                 "join_date": "2020-05-24"
         }
    ]
}
```
## Installation

To install the Web API on your local machine, run the following commands(from your desired folder):
```bash
# Clone the git repo
git clone https://github.com/TeeblaQ1/employeeAPI.git

# Install requirements 
# (this can be done directly or by first creating a virtual environment)
pip install -r requirements.txt


# (NOTE: The next set of commands must be executed at the level where the \
# manage.py file is located.)
# Create database (default SQLite) and migrate to add all apps to database
python manage.py migrate

# Make migrations to the entities app and migrate to database afterwards
python manage.py makemigrations entities
python manage.py migrate

# Create superuser to login to admin page. (Fill in credentials as prompted)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## Testing

The application has been tested with the traditional ```python manage.py test``` to confirm that only logged in users can create, update or delete a post and that in fact, the changes made were exact using the methods in the TestCase class like the ```self.assertEqual``` method. 
The authentication and authorization were not tested since it uses already-tested third-party apps and frameworks and we'd like to keep everything DRY.

## Security

The employeeAPI is highly secure because it is built upon and using a highly secure framework - Django Rest Framework. Extra layers of security were added to ensure that only logged in users can carry out POST, PUT or DELETE on the database and only allows for GET requests from guests (unauthorized users).

## Scalability

The employeeAPI allows for scalability both vertically and horizontally as it contains features that allows our application to be stateless. Third party services are used for all states. E.g. Database, caching etc. The database for instance can be changed from the default SQLite database to another database running on another server instance.  Also, since Django is pluggable, we can replace existing "built-in" features with a custom feature we want to add support for in later times.

## Limitations

The major limitation in these RESTful API is that the authorization and authentication does not fully have a view and template name for functionalities around password reset, password confirm, password change etc. So for now, only superuser can carry out those operations for all users. These can be addressed by creating an account app that is linked with it and caters for all these things. The new features will be available in v2 of this app.

## Documentation

A third-party package (Swagger) has been used to implement the OpenAPI Specification. This includes the detailed description of every feature, how to use it, the parameters it takes as well as a try out for all features. To view the documentation on your local machine, run the server locally using the command below (at the level where the ```manage.py``` file is):
```bash
python manage.py runserver
```

## Deployment

The employeeAPI has been deployed on [Heroku](https://heroku.com) and is available at [employeeAPI](https://employeewebapi.herokuapp.com/).
Please carefully read documentations on the [homepage](https://employeewebapi.herokuapp.com/) to know how best to navigate the RESTful API.
It is also worthy of note that the detailed view of each entity is generated using its unique employee_id (as opposed to traditional id) as you will find in the documentations.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
