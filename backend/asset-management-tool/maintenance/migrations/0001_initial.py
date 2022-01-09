# Generated by Django 3.1.7 on 2021-08-12 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config_pannel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('possible_failure', models.CharField(blank=True, max_length=250, null=True)),
                ('maintenance_cost', models.FloatField()),
                ('maintenance_action', models.CharField(choices=[('Replace', 'REPLACE'), ('Paint', 'PAINT'), ('Reinforce', 'REINFORCE')], max_length=50)),
                ('maintenance_interval_from', models.DateField()),
                ('maintenance_interval_to', models.DateField()),
                ('impact_of_failure', models.CharField(max_length=250)),
                ('possibility_of_failure', models.CharField(choices=[('High', 'HIGH'), ('Medium', 'MEDIUM'), ('Low', 'LOW')], max_length=50)),
                ('resulting_risk_score', models.FloatField()),
                ('mitigation', models.CharField(choices=[('Preventive', 'PREVENTIVE'), ('Inspection', 'INSPECTION'), ('Reactive', 'REACTIVE')], max_length=50)),
                ('next_action_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AssetComponentLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField()),
                ('problem', models.CharField(max_length=200)),
                ('action', models.CharField(max_length=250)),
                ('duration', models.IntegerField()),
                ('cost_total', models.FloatField()),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='asset_component_log', to='maintenance.assetcomponent')),
                ('supply_belt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asset_comp_log', to='config_pannel.supplybelts')),
            ],
        ),
        migrations.CreateModel(
            name='AssetComponentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('water_scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset_component_category', to='config_pannel.waterscheme')),
            ],
        ),
        migrations.AddField(
            model_name='assetcomponent',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_asset_component', to='maintenance.assetcomponentcategory'),
        ),
    ]
