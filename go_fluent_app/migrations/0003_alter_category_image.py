# Generated by Django 3.2.2 on 2021-05-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go_fluent_app', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.TextField(null=True),
        ),
    ]