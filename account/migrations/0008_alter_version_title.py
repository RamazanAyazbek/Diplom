# Generated by Django 4.1.5 on 2023-04-04 06:45

from django.db import migrations, models
from django.apps import apps

def set_default_title(account, schema_editor):
    PostVersion = apps.get_model('account', 'Version')
    PostVersion.objects.filter(title=None).update(title='Untitled')

class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_version_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='title',
            field=models.CharField(default='Untitled', max_length=200),
            preserve_default=False,
        ),
         migrations.RunPython(set_default_title),
    ]
