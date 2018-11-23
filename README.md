# PyBook
Python project for Makers AceBook

Authors, Neil, Preeti, David, Sundar.

----------------------------------------------------------------------------------------

Prerequisites,
----------------
1. [Python 3.7.1 Installation notes](https://www.python.org/downloads/release/python-371/)
2. [Brew (Homebrew Installer)](https://brew.sh)
3. [PIP Installer](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjNmoGZ4eLeAhWKJcAKHSYwCZIQFjAAegQIChAB&url=https%3A%2F%2Fpip.pypa.io%2Fen%2Fstable%2Finstalling%2F&usg=AOvVaw0rFf39yx8FcmyDOcIiD8w0)

After creating virtual env ensure you have the following installed

- BDD
    - mamba
    - expects

- Web Framework
    - Django

- Django ORM for MongoDB
    - Djongo
    - MongoDB

----------------------------------------------------------------------------------------
Setting up Virtual Enviroment
------------------------------
 If virtual enviroment is required perform below steps,

> Virtual enviroment after project dir exists. 'env' in the command below can be any directory. It gets created
> if it does not exist already
```
virtualenv -p /usr/local/bin/python3 env
source env/bin/activate
```
----------------------------------------------------------------------------------------
MongoDB installation notes.
----------------------------

To install perform the below steps,

> Activate your virtual environment and issue the below from within the virtual environment
```pip install mongodb```

> Make ```db``` directory structure in project folder,
```cd pybook directory
mkdir -p ./db
```
> Running MongoDB in background, use ```ps -eaf | grep mongo``` (this gets process id to kill if needed and start it)
> start Daemon specifying DB path location, open a shell and type. Using an ampersand at the end will ensure the deamon 
> runs in the background and the terminal can be reused if need be

```mongod --dbpath ./db &```

> Start MongoDB command line, open another shell and type 
```
   > mongo
   > use pybook_test
   > db.createCollection("users")
   > show collections
   > db.users.insert({ user_name: "joe bloggs", email: "joe.bloggs@makers.com", user_message: "Hello World!"})
   > db.users.find()
```
----------------------------------------------------------------------------------------------------------------
Django Install & Setup
-----------------------

*Note* Django follows the Model-Template-View frameork, application gets data from the model, view uses the data and then renders web template containing processed information, Django views has likeness of controllers akin to MVC.

From within Project directory,
-----------------------------
1. Installing Django

    ```pip install django```

2. Installing Djongo

    ```pip install djongo```

3. Installing [BDDs](https://github.com/nestorsalceda/mamba) 
    ```pip install mamba
       pip install expects
    ```

4. Installing MongoDB
```
    pip install mongodb
    mongod --dbpath ./db &
```
> note db is a folder you created inside your project path
 

5. Running Django
> from inside the folder that has migrate.py.
``` 
python manage.py migrations
python manage.py runserver
```
    
>if you see errors or text in red after running server, stop the process and ensure the missing libraries/packages or steps are followed before attempting to access the page

```[Application](http://localhost:8000)```
--------------------------------------------------------------------------------------------------------------------
References
----------
```
 Setting up Django,
    > For the first ti
    django-admin startproject helloapp

    once done direcotry structure will look like below,

            helloapp
        ├─helloapp
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py

        helloapp and manage.py are the main project folder, settings sre in settigns.py and routes are in urls.py.

        Create new by cd into helloapp directory and type > python manage.py startapp myapp, it will create folder within called myapp

        Django will only regonise new application if addded to settign file, under INSTALLED APPS.

        To run Django, type python manage.py runserver, then access via [localhost](http://localhost:8000)
```
