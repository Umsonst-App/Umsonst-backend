# Generated by Django 5.1 on 2024-12-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_complaint_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=60, unique=True, verbose_name='email'),
        ),
    ]
