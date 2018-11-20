# PyBook
Python project for Makers AceBook

Authors, Neil, Preeti, David, Sundar.

----------------------------------------------------------------------------------------

- Prerequisites,

    Python 3.7.1 Installation notes,
    https://www.python.org/downloads/release/python-371/

    Brew (Homebrew Installer)
    https://brew.sh

    PIP Installer
    https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjNmoGZ4eLeAhWKJcAKHSYwCZIQFjAAegQIChAB&url=https%3A%2F%2Fpip.pypa.io%2Fen%2Fstable%2Finstalling%2F&usg=AOvVaw0rFf39yx8FcmyDOcIiD8w0

----------------------------------------------------------------------------------------

MongoDB installation notes.

To install perform the below steps,

1. brew update.

2. brew install mongodb

3. make DB direcotry structure in project folder,
    cd pybook directory
    mkdir -p ./data/db

4. Running MongoDB,
    start Daemon specifying DB path location, open a shell and type >
    mongod --dbpath ./data/db

5. Start MongoDB command line,
    open another shell and type > mongo

----------------------------------------------------------------------------------------
Setting up Virtual enviroment

1. If virtual enviroment is required perform below steps,

    option 1.
    Virtual enviroment after project dir exists
    virtualenv -p /usr/local/bin/python3 env
    source env/bin/activate

    option 2 (preferred for now).
    Setting up enviroment
    brew install pyenv
    pyenv install 3.7.1
    pyenv global 3.7.1
    pyenv shell 3.7.1

----------------------------------------------------------------------------------------

Django Install & Setup

Note Django follows the Model View, application gets data from the model, view uses the data and then renders web template containing processed information, Django views has likeness of controllers with MVC.

From within Project directory,

1. Installing Django,

    pip install django

2. Setting up Django,

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

        To run Django, type python manage.py runserver, then access via http://localhost:8000








----------------------------------------------------------------------------------------
Mamba install

    Some note were taken from here > https://github.com/nestorsalceda/mamba

1.  Mamba enviroment setup,
    pipenv install mamba

2.  Installion of Mamba,
    pip install mamba

3.  Add Python module for expects,
    pipenv install expects

    # the above commands generate pipfile and pipfile.lock akin to the gemfile & gemfile.lock
    #save the spec in a .py file and execute it as follows
