# Generated by Django 3.1.7 on 2023-06-08 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date_added',)},
        ),
    ]
