# Generated by Django 5.2 on 2025-05-05 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model'], 'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['-number_of_wins', 'name'], 'verbose_name': 'Driver', 'verbose_name_plural': 'Drivers'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['team_name'], 'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.RemoveField(
            model_name='team',
            name='driver',
        ),
        migrations.AddField(
            model_name='driver',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='drivers/', verbose_name='Driver Photo'),
        ),
        migrations.AddField(
            model_name='team',
            name='driver1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_teams', to='library.driver', verbose_name='First Driver'),
        ),
        migrations.AddField(
            model_name='team',
            name='driver2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='secondary_teams', to='library.driver', verbose_name='Second Driver'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=45, verbose_name='Car Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.team', verbose_name='Owning Team'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='name',
            field=models.CharField(error_messages={'blank': 'Driver name must be provided'}, help_text='Enter the full name of the driver', max_length=45, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='nationality',
            field=models.CharField(help_text='Enter the driver’s nationality', max_length=45, verbose_name='Nationality'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='number_of_wins',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of Wins'),
        ),
        migrations.AlterField(
            model_name='team',
            name='country',
            field=models.CharField(max_length=45, verbose_name='Country of Origin'),
        ),
        migrations.AlterField(
            model_name='team',
            name='engine_supplier',
            field=models.CharField(choices=[('Ferrari', 'Ferrari'), ('Mercedes', 'Mercedes'), ('Honda', 'Honda'), ('Renault', 'Renault')], max_length=20, verbose_name='Engine Supplier'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=45, verbose_name='Team Name'),
        ),
    ]
