from .models import Authenticate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

#Everytime a user is created or is saved we save its data
@receiver(post_save, sender=User)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        Authenticate.objects.create(user=instance)