from django.db import models

from qwitter import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE
    )
    follows = models.ManyToManyField(
        'self', related_name='followed_by', symmetrical=False, blank=True
    )

    def __str__(self):
        return self.user.username


class Qweet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='qweets', on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:50]}..."
        )
