# Generated by Django 3.1.7 on 2021-08-18 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_assetcomponentlog_componant_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetcomponent',
            name='water_scheme',
        ),
    ]
