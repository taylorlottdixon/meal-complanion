# Generated by Django 4.2.4 on 2023-08-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_ingredient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='main_app.ingredient'),
        ),
    ]
