# Generated by Django 3.1.14 on 2022-02-08 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_following'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Following',
        ),
    ]
