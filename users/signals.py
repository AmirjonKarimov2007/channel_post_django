from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Nomzot_Ovozlar, Nomzodlar

@receiver(post_save, sender=Nomzot_Ovozlar)
def create_profile(sender, instance, created, **kwargs):
    if created:
        nomzod = instance.nomzod
        nomzod.ovozlar = nomzod.nomzot_ovozlar.count()
        nomzod.save()

@receiver(post_delete, sender=Nomzot_Ovozlar)
def delete_user(sender, instance, **kwargs):
    nomzod = instance.nomzod
    nomzod.ovozlar = nomzod.nomzot_ovozlar.count()
    nomzod.save()