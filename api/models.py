from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """Represents User which is extended base User"""
    last_activity = models.DateTimeField(default=timezone.now, null=False)


class Post(models.Model):
    """Represents post"""
    title = models.CharField(max_length=300)
    body = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='posts')
    likes_amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post {self.title}'


class Like(models.Model):
    """Represent user's likes per post"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    created_at = models.DateTimeField(auto_now_add=True)
