# Generated by Django 3.1.6 on 2022-01-24 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20211025_1608'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Home_Layout',
        ),
        migrations.DeleteModel(
            name='Intrest',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Technology',
        ),
        migrations.RemoveField(
            model_name='portfolio_post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='portfolio_post',
            name='image3',
        ),
    ]
