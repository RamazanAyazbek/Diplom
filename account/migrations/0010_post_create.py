# Generated by Django 4.1.5 on 2023-04-13 05:01
from django.apps import apps
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_version_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
