# Generated by Django 5.0.6 on 2024-07-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0004_remove_item_city_remove_item_country_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sharecircle",
            name="flagged",
        ),
        migrations.AddField(
            model_name="item",
            name="flagged",
            field=models.BooleanField(default=False),
        ),
    ]