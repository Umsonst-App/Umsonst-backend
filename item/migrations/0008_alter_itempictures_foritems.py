# Generated by Django 5.0.6 on 2024-08-22 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0007_remove_item_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itempictures",
            name="forItems",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="item.item",
            ),
        ),
    ]
