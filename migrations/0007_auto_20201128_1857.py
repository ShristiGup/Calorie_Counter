# Generated by Django 3.1.1 on 2020-11-28 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201128_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfooditems',
            name='meal_cat',
            field=models.ForeignKey(default='Breakfast', null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.mealcategory'),
        ),
    ]
