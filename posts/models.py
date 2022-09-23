from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from category.models import Category


class Post(models.Model):
    """ For when user creates a post.
    the price can't go below 0 or above 100000, if it does
    then raise an error.

    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True, blank=False)
    image = models.ImageField(upload_to='images/',
                              default='../default-post_oi2vmt', blank=True)
    pros = models.TextField(max_length=400, blank=False, default="")
    cons = models.TextField(max_length=400, blank=False, default="")
    content = models.TextField(max_length=2000, blank=False)
    price = models.PositiveIntegerField(
        blank=True,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    category = models.ForeignKey(Category,
                                 related_name="posts",
                                 on_delete=models.CASCADE,
                                 blank=False, null=False, default=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.title}'
