# Generated by Django 3.1.6 on 2021-03-12 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_category_portfolio_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portfolio_Post',
        ),
    ]