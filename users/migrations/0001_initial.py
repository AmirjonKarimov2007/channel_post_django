# Generated by Django 5.0 on 2024-11-09 17:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomzodlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='ism familiya')),
                ('ovozlar', models.BigIntegerField(blank=True, default=0, null=True, verbose_name='ovozlar soni')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Fullname')),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Username')),
                ('user_id', models.BigIntegerField(default=1, unique=True, verbose_name='Telegram_id')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='sarlavha')),
                ('channel', models.CharField(blank=True, max_length=200, null=True)),
                ('message_id', models.BigIntegerField(blank=True, null=True, verbose_name='message id')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='Yaratilgan sana')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Tugash sanasi va vaqti')),
                ('nomzodlar', models.ManyToManyField(blank=True, to='users.nomzodlar')),
            ],
        ),
        migrations.CreateModel(
            name='Nomzot_Ovozlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.BigIntegerField(verbose_name='Telegram_id')),
                ('nomzod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomzot_ovozlar', to='users.nomzodlar')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nomzot_ovozlars', to='users.post')),
            ],
        ),
        migrations.AddField(
            model_name='nomzodlar',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='nomzodlars', to='users.post'),
        ),
        migrations.CreateModel(
            name='SendPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=100, verbose_name='message id')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='Yaratilgan sana')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Tugash sanasi')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.post')),
            ],
        ),
    ]
