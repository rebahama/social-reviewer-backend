from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model, owner have one instance to the user and
       the images is uploaded to cloudinary host service, if no
       picture is uploaded a default image will be provided.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/',
    default='../default-avatar_e6z9oo', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

