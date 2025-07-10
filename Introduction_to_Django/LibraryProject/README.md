## Initializing Django Project

- install django: `pip install django`
- Create a django project `django-admin startproject LibraryProject`
- Navigate into project directory `cd LibraryProject`
- Start development server `python manage.py runserver`
- Create a django app `python manage.py startapp bookshelf`
- Create models in `\bookshelf\models.py`
- Register models in  `\bookshelf\admin.py`
- Register bookshelf app in `LibraryProject/settings.py`
- Create migration files `python manage.py makemigrations bookshelf`
- Make migrations `python manage.py migrate`