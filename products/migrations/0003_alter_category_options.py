# Generated by Django 3.2 on 2022-03-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_produtct_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]