# Generated by Django 2.1.5 on 2019-11-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDecisionTreeBasedTourism', '0003_auto_20191118_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel_packages',
            old_name='City',
            new_name='Suitable_group',
        ),
        migrations.RemoveField(
            model_name='travel_packages',
            name='Suitable_for',
        ),
        migrations.AddField(
            model_name='travel_packages',
            name='Suitable_State',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]