# Generated by Django 5.0.6 on 2024-06-20 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_suppliers_inventoryitems_suppliers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitems',
            name='suppliers',
            field=models.ManyToManyField(related_name='inventory_items', to='core.suppliers'),
        ),
    ]
