# Generated by Django 4.1.5 on 2023-04-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_posthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='posthistory',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
