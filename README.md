## CUSTOM COMMANDS

### Create fake user python

python manage.py create_users 5 

### Deleter users (except superuser)

python manage.py delete_users 1 2 3 4 5

### Fixtures

fixtures.json


### Graph_models
#To group all the application and output into PNG file
$ python manage.py graph_models -a -g -o imagefile_name.png
#Include only some applications
$ python manage.py graph_models app1 app2 -o app1_app2.png
#Include only some specific models
$ python manage.py graph_models -a -I Foo,Bar -o foo_bar.png
#OR exclude certain models 
$ python manage.py graph_models -a X Foo,Bar -o no_foo_bar.png

