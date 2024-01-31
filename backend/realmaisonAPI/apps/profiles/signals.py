from realmaisonAPI.settings.base import AUTH_USER_MODEL
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"User {instance.username} profile created")


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"User {instance.username} profile saved")
    return instance
