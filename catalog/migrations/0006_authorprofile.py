# Generated by Django 4.1.5 on 2023-01-30 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_dob_author_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=255, verbose_name='Bio of author')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.author')),
            ],
        ),
    ]
