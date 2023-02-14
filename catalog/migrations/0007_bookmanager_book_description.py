# Generated by Django 4.1.5 on 2023-02-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_authorprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, verbose_name='About book'),
        ),
    ]
