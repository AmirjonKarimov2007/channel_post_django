# Generated by Django 5.1.2 on 2024-11-05 06:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]