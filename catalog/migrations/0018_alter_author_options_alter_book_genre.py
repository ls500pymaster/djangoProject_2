# Generated by Django 4.1.6 on 2023-02-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20230207_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.genre'),
        ),
    ]
