# Generated by Django 5.0.6 on 2024-07-15 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_message_created_at_unix"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="created_at_unix",
        ),
    ]