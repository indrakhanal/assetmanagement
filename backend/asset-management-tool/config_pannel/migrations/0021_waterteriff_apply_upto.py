# Generated by Django 3.1.7 on 2021-09-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_pannel', '0020_usebasedunitrange'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterteriff',
            name='apply_upto',
            field=models.DateField(blank=True, null=True),
        ),
    ]
