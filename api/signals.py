from django.dispatch import receiver
from django.db.models.signals import post_save

from api.models import (
    Post,
    Like
)


@receiver(post_save, sender=Like)
def update_likes_amount(sender, instance, created, **kwargs):
    if not created:
        Post.objects.get()
