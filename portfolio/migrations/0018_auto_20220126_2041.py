# Generated by Django 3.1.6 on 2022-01-26 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_auto_20220124_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio_post',
            old_name='category',
            new_name='tools_used',
        ),
    ]
