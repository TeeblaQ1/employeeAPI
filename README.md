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
## Testing

The application has been tested to confirm that only logged in users can create, update or delete a post and that in fact, the changes made were exact using the ```self.assertEqual``` method. 
The authentication and authorization were not tested since it uses already-tested third-party apps and frameworks.

## Security

The employeeAPI is highly secure because it is built upon and using a highly secure framework - Django Rest Framework. Extra layers of security were added to ensure that only logged in users can carry out POST, PUT or DELETE on the database and only allows for GET requests from guests (unauthorized users).

## Scalability

The employeeAPI allows for scalability both vertically and horizontally as it contains features that allows our application to be stateless. Third party services are used for all states. E.g. Database, caching etc. The database for instance can be changed from the default SQLite database to another database running on another server instance.  Also, since Django is pluggable, we can replace existing "built-in" features with a custom feature we want to add support for in later times.

## Limitations

The major limitation in these RESTful API is that the authorization and authentication does not fully have a view and template name for functionalities around password reset, password confirm, password change etc. These can be addressed by creating an account app that is linked with it and caters for all these things. The new features will be available in v2 of this app.

## Documentation

A third-party package (Swagger) has been used to implement the OpenAPI Specification. This includes the detailed description of every feature, how to use it, the parameters it takes as well as a try out for all features. To view the documentation on your local machine, run the server locally using the command below (at the level where the ```manage.py``` file is):
```bash
python manage.py runserver
```

## Deployment

The employeeAPI has been deployed on [Heroku](https://heroku.com) and is available at [employeeAPI](https://employeewebapi.herokuapp.com/).
Please carefully read documentations to know how best to navigate the RESTful API.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
