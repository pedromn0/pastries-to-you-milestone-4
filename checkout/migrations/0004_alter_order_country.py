# Generated by Django 3.2 on 2022-04-04 17:10

import checkout.models
from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220404_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(countries=checkout.models.Ireland, max_length=2),
        ),
    ]
