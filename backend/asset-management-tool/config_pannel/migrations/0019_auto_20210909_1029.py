# Generated by Django 3.1.7 on 2021-09-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config_pannel', '0018_qualitytestparameter_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waterteriff',
            old_name='year_from',
            new_name='apply_date',
        ),
        migrations.RemoveField(
            model_name='waterteriff',
            name='estimated_paying_connection',
        ),
        migrations.RemoveField(
            model_name='waterteriff',
            name='unit_from',
        ),
        migrations.RemoveField(
            model_name='waterteriff',
            name='unit_to',
        ),
        migrations.RemoveField(
            model_name='waterteriff',
            name='used_base_rate',
        ),
        migrations.RemoveField(
            model_name='waterteriff',
            name='year_to',
        ),
        migrations.AddField(
            model_name='supplybelts',
            name='coverage_area',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='waterteriff',
            name='estimated_paying_connection_household',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='waterteriff',
            name='estimated_paying_connection_institution',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='waterteriff',
            name='rate_for_household',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='waterteriff',
            name='rate_for_institution',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
