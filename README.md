# Magic of programming
Magic of programming is a web app project that allows user to create their project portfolio. It was developed with ` python 3.9` and `Django 3.1.3`.

## Getting started
Use `pip` and `requirements.txt` file to install packages: 

```bash
pip install -r requirements.txt
```

By default, the app uses SQLite for data storage. Before deploying on a production server, switch the database engine for security and performance.

For testing convenience, SQLite file was added. For testing convenience, SQLite file was added. You can use an already existing admin account to access the administration panel:
```
localhost:8000/admin
login: admin
password: test
```
Alternatively, you can create superuser from a console:
```python manage.py createsuperuser```

Once this command completes a new superuser will have been added to the database. Now restart the development server so we can test the login:

```python3 manage.py runserver```


## Additional packages
### Django CKEditor
Provides an easy way to add rich text editor to Django admin. 
Used for:
* blog post
* project description
* hobbies 
### Django Phonenumber Field
A Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers. python-phonenumbers is a port of Google's libphonenumber library, which powers Android's phone number handling.
### Django Solo
A Django library that helps working with singletons. Added to the project for the managing site configuration. It provides changes to the Django admin panel along with the singleton model type. 
