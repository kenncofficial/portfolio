# Generated by Django 3.1.6 on 2021-02-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
