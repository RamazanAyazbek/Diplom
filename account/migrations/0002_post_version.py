# Generated by Django 4.1.5 on 2023-03-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
