# Generated by Django 3.2.16 on 2023-02-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_author_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('method', models.CharField(max_length=5)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('exec_time', models.IntegerField(null=True)),
                ('author', models.CharField(max_length=255)),
            ],
        ),
    ]
