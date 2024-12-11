from tabnanny import verbose

from django.db import models
from django.db.models import ForeignKey, PROTECT
from django.utils import timezone
from django.db.models import Sum
from django.core.exceptions import ValidationError

class User(models.Model):
    name = models.CharField(verbose_name='Fullname', max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True)
    user_id = models.BigIntegerField(verbose_name='Telegram_id', unique=True, default=1)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan sana")
    def __str__(self):
        return self.name

class Nomzodlar(models.Model):
    fullname = models.CharField(max_length=200, verbose_name='ism familiya')
    ovozlar = models.BigIntegerField(default=0,blank=True,null=True, verbose_name='ovozlar soni')
    posts = models.ForeignKey('Post', on_delete=models.DO_NOTHING, related_name='nomzodlars')

    def __str__(self):
        return str(f"{self.fullname}| {self.ovozlar}")


class Nomzot_Ovozlar(models.Model):
    telegram_id = models.BigIntegerField(verbose_name='Telegram_id')
    nomzod = models.ForeignKey(Nomzodlar, on_delete=models.CASCADE, related_name='nomzot_ovozlar')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='nomzot_ovozlars')
    def __str__(self):
        return str(f"{self.telegram_id}")
class Post(models.Model):
    nomzodlar = models.ManyToManyField(Nomzodlar,blank=True)
    title = models.CharField(max_length=200, verbose_name='sarlavha')
    channel = models.CharField(max_length=200, null=True, blank=True)
    message_id = models.BigIntegerField(unique=False, null=True, blank=True, verbose_name='message id')
    pin = models.BooleanField(default=False,blank=True)
    created_date = models.DateField(default=timezone.now, verbose_name='Yaratilgan sana')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Tugash sanasi va vaqti')

    def __str__(self):
        return self.title



class SendPost(models.Model):
    message_id = models.CharField(max_length=100, verbose_name='message id')
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    created_date = models.DateField(default=timezone.now, verbose_name='Yaratilgan sana')
    end_date = models.DateField(null=True, blank=True, verbose_name='Tugash sanasi')  # Optional field

    def __str__(self):
        return str(self.message_id)
