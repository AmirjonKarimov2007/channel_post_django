# Generated by Django 5.0 on 2024-11-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pin',
            field=models.BooleanField(default=False, verbose_name='pin'),
        ),
    ]