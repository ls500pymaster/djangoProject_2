## Overview

![](https://github.com/ls500pymaster/djangoProject_2/blob/master/catalog.png?raw=true)

## Custom commands

### Create fake book

```bash
python3 manage.py create_book 100
```

### Create fake author

```bash
python3 manage.py create_author 100
```

### Create fake user

```bash
python manage.py create_users 5 
```
### Deleter users (except superuser)

```bash
python manage.py delete_users 1 2 3 4 5
```
### Fixtures

fixtures.json

```bash
python manage.py dumpdata --all --indent 2 -o fixtures.json
```

### Runserver
```bash
python manage.py runserver --insecure
```

Debug mode False, because I need to load statics for custom 404 error page

### Django model forms
` http://127.0.0.1:8000/catalog/author/2/
` Author, Edited

` http://127.0.0.1:8000/catalog/book/new/
` Add new book

` http://127.0.0.1:8000/catalog/
` All books

` http://127.0.0.1:8000/crm/
` CRM app. Using annotate, aggregate, prefetch related, select related

#### ### Graph_models

To group all the application and output into PNG file
`python manage.py graph_models -a -g -o imagefile_name.png
`

Include only some applications
`python manage.py graph_models app1 app2 -o app1_app2.png`

Include only some specific models
`python manage.py graph_models -a -I Foo,Bar -o foo_bar.png`

OR exclude certain models 
`python manage.py graph_models -a X Foo,Bar -o no_foo_bar.png`


## Docker Rabbitmq, Redis

` docker run -d -p 5672:5672 rabbitmq
` 

`  docker run -d -p 6379:6379 redis
` 

## Rabbitmq

MacOS install with brew

` brew install rabbitmq
` 

Localhost address and port

`
http://localhost:15672/
guest:guest
` 

Rabbitmq info command

`
brew info rabbitmq
` 

To start a node in the background, use

`
brew services start rabbitmq
` 

To stop

`
brew services stop rabbitmq
` 

## Redis

` brew install redis
` 

Start server in background

` brew services start redis
` 

Check info about running redis service

` brew services info redis
` 

To stop the service

` brew services stop redis
` 

# Create a regular user 'foo'
>>> user = User.objects.create_user('foo', 'foo.bar@xxx.com', 'bar')

# List all users
>>> User.objects.all()
[<User: admin>, <User: abegail>, <User: foo>]

>>> User.objects.all()[1].is_superuser
True

>>> User.objects.all()[2].is_superuser
False

# Drop a user from the db
>>> User.objects.all()[2].delete()

>>> User.objects.all()
[<User: admin>, <User: abegail>]

# Create a superuser
>>> user = User.objects.create_superuser('burr', 'burr@buzz.com', 'buzz')

>>> User.objects.all()
[<User: admin>, <User: abegail>, <User: burr>]

>>> User.objects.all()[2].delete()

>>> User.objects.all()
[<User: admin>, <User: abegail>]


## Celery example Django ORM


` from crm import tasks
` 

` from crm.tasks import add
` 

` add.delay(1,4)
` 

##### <AsyncResult: f7bd8bbb-eb76-452c-992a-d807b455da24>

