# Generated by Django 3.1.1 on 2020-11-28 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_fooditems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodItems',
            new_name='UserFoodItems',
        ),
        migrations.AlterModelOptions(
            name='mealcategory',
            options={'verbose_name_plural': 'Meal Categories'},
        ),
        migrations.AlterModelOptions(
            name='plancategory',
            options={'verbose_name_plural': 'Plan Categories'},
        ),
        migrations.AlterModelOptions(
            name='userfooditems',
            options={'verbose_name': 'User Food Item'},
        ),
    ]
