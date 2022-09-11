from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileLikes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, related_name='profile_likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'profile']

    def __str__(self):
        return f'{self.owner} {self.profile}'
