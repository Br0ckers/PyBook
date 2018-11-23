# PyBook
Python project for Makers AceBook

**Authors**
- Neil
- Preeti
- David
- Sundar

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
```
cd pybook directory
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

*Note Django follows the Model-Template-View frameork, application gets data from the model, view uses the data and then renders web template containing processed information, Django views has likeness of controllers akin to MVC.*

From within Project directory,
-----------------------------
1. Installing Django

```pip install django```

2. Installing Djongo

```pip install djongo```

3. Installing [BDDs](https://github.com/nestorsalceda/mamba) 
```
pip install mamba
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

[Application](http://localhost:8000)

--------------------------------------------------------------------------------------------------------------------
Sequence of Changes to the Django-Djongo (MongoDB Wrapper for Django)
---------------------------------------------------------------------

1. Create app using ```./manage.py startapp msg_board```
2. In the settings.py of the pybookapp folder update the following
```
    DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'pybook_test1',
       }
   }
```

3. In the urls.py of the pybookapp update the following - see the second line to include the *msg_board.urls*
```
    urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('msg_board.urls')),
]
```

4. In the msg_board folder update the *models.py* and include the following
```
    from djongo import models
```

and create a model. Django model is the MongoDB's representation of collection (table). The Model created through
Django in its plural form become the collection in MongoDB for example Model *Player* becomes *players* collection.
If Django were to manage your DB the collections will be created in the following format *containername_appname_modelS*
*pybookapp_msg_board_players* 

```
    class Player(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user_message = models.CharField(max_length=100)
    objects = models.DjongoManager()

    def __str__(self):
        return self.user_name
```

5. Next step is to register your model in the admin.py of the msg_board, hence update it as follows

```
    admin.site.register([Player])
```

6. Update your app.py under msg_board with the following

```
    class MsgBoardConfig(AppConfig):
        name = 'msg_board'
```

7. Update your views in the msg_board with the following changes
> include the views
```
    from msg_board.models import Player

```
> and update the following

```
class UserListProperView(TemplateView):
    def get(self, request, **kwargs):
        print("Fetching users via Djongo")
        player = Player.objects.all()
        print(player)
        print(len(player))
        print(dir(player))
        data = {}
        data['object_list'] = player
        return render(request, 'player.html', {"data": data})
```

8. finally in your urls.py of the msg_board make the following changes
> include the views
```
    from msg_board import views
```
> and update the url patterns
```
    urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^user', views.UserListView.as_view()),
    url(r'^player', views.UserListProperView.as_view()),

]
```

References to a setting up a django project from scratch
--------------------------------------------------------
```
 Setting up Django,
    > For the first time
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