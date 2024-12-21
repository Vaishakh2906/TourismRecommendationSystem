# Generated by Django 2.1.5 on 2019-11-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDecisionTreeBasedTourism', '0009_user_review_productid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel_packages',
            old_name='Suitable_State',
            new_name='Suitable_City',
        ),
        migrations.AddField(
            model_name='user_review',
            name='City',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='user_bookings',
            name='City',
            field=models.CharField(default=None, max_length=50),
        ),
    ]