# Generated by Django 3.1.7 on 2021-09-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0015_auto_20210905_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentinfo',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
