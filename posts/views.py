from django.shortcuts import render
from rest_framework import generics
from social_drf.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializer import PostSerializer


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

