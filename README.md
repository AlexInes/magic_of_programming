#Magic of programming
Magic of programming is a web app project that allows user to create their project portfolio. It was developed with ` python 3.9` and `Django 3.1.3`.

##Getting started
Virtual Environment files are included in a `venv` folder for fast deployment. Alternatively, use `pip` and `requirements.txt` file to install packages: 

```bash
pip install -r requirements.txt
```

By default, the app uses SQLite for data storage. Before deploying on a production server, switch the database engine for security and performance.

##Additional packages
###Django CKEditor
Provides an easy way to add rich text editor to Django admin. 
Used for:
* blog post
* project description
* hobbies 
###Django Phonenumber Field
A Django library which interfaces with python-phonenumbers to validate, pretty print and convert phone numbers. python-phonenumbers is a port of Google's libphonenumber library, which powers Android's phone number handling.
###Django Solo
A Django library that helps working with singletons. Added to the project for the managing site configuration. It provides changes to the Django admin panel along with the singleton model type. 
