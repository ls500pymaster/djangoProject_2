# Generated by Django 3.2.16 on 2023-02-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_requestlog_body_unicode'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlog',
            name='data',
            field=models.CharField(max_length=255, null=True),
        ),
    ]