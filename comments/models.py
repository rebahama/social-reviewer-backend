from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comments(models.Model):
    RATING = ((1, 'Very bad',),
              (2, 'bad'),
              (3, 'good'),
              (4, 'Very good'),
              (1, 'Extremely good'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(blank=True,
             default=3, choices=RATING)
    content = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content + ' ' + str(self.owner)