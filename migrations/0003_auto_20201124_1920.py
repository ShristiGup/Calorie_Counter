# Generated by Django 3.1.1 on 2020-11-24 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_meal_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meal_Category',
            new_name='MealCategory',
        ),
    ]
