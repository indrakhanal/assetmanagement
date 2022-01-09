# Generated by Django 3.1.7 on 2021-08-25 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0011_auto_20210824_0703'),
        ('finance', '0004_auto_20210815_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='maintenance_expense',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maintenance.componentinfolog'),
        ),
    ]
