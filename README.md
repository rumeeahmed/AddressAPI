# AddressApi

To create a DRF app first create a project using the command 
`django-admin start project {project name}`.

Then go into that directory and make a migration by using `python
manage.py migrate`

Then create an app with `python manage.py startapp {app name}`

Then create a superuser using `python manage.py superuser`

Before sending a json from the API to the client the data needs to
be serialized into JSON data.