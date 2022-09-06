from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """ For when user creates a post.

    """

    SUBJECT = (('Sports', 'Sports'),
               ('Movies', 'Movies'),
               ('Vehicles', 'Vehicles'),
               ('Electronics', 'Electronics'),
               ('Clothes', 'Clothes'),
               ('Other,', 'Other')
               )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False)
    image = models.ImageField(upload_to='images/',
    default='../default-post_oi2vmt', blank=True)
    content = models.TextField(max_length=1600, blank=False)
    category = models.CharField(max_length=20,
    choices=SUBJECT, default='Other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.title}'
