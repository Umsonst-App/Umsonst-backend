# Generated by Django 5.1 on 2025-01-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='item_notifications',
            field=models.BooleanField(default=True),
        ),
    ]