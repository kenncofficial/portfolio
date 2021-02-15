# Generated by Django 3.1.6 on 2021-02-15 19:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_intrest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
