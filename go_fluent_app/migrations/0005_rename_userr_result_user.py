# Generated by Django 3.2.2 on 2021-05-17 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go_fluent_app', '0004_auto_20210517_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='userr',
            new_name='user',
        ),
    ]
