# Generated by Django 5.1.2 on 2024-11-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_rename_nomzodlarr_post_nomzodlar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.CharField(blank=True, default='https://i.imghippo.com/files/Kih9983kr.jpg', max_length=200, null=True, verbose_name='post rasmi'),
        ),
    ]
