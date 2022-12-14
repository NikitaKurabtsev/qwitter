from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from qwitter import settings
from qwitter_app.models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
