# Generated by Django 3.1.7 on 2021-09-15 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config_pannel', '0023_auto_20210915_0728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yearsinterval',
            options={'verbose_name': 'Year Interval', 'verbose_name_plural': 'Year Intervals'},
        ),
        migrations.RenameField(
            model_name='yearsinterval',
            old_name='schema',
            new_name='scheme',
        ),
    ]
