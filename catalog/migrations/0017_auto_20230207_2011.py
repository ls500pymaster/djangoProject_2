# Generated by Django 3.2.16 on 2023-02-07 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_requestlog_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestlog',
            old_name='body_unicode',
            new_name='body_get',
        ),
        migrations.RenameField(
            model_name='requestlog',
            old_name='data',
            new_name='body_post',
        ),
    ]
