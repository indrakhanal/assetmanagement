# Generated by Django 3.1.7 on 2021-11-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_pannel', '0041_auto_20211118_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherexpense',
            name='apply_upto',
            field=models.DateField(blank=True, null=True),
        ),
    ]
