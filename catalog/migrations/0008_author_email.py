# Generated by Django 4.1.5 on 2023-02-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_bookmanager_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Author email'),
        ),
    ]
