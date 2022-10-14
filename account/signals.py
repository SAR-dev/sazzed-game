from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Account
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(pre_save, sender=Account)
def save(sender, instance, *args, **kwargs):
    if instance.avatar:
        try:
            acc = Account.objects.get(id=instance.id)
            pre = acc.avatar
            post = instance.avatar
            if (pre != post and pre != "images/avatar.jpg"):
                pre.delete(save=True)
        except:
            pass