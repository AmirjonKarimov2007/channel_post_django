# Generated by Django 5.0 on 2024-11-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_post_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pin',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='pin'),
        ),
    ]
