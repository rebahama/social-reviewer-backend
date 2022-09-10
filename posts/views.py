from django.db.models import Count
from rest_framework import generics, permissions, filters
from social_drf.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializer import PostSerializer


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(like_counter=Count('likes', distinct=True),
    comment_counter=Count('comments', distinct=True)).order_by('-created_at')

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = [
        'likes_counter',
        'comment_counter',
        'category__id',
        'price'

    ]
    search_fields = [
        'owner__username',
        'title',
        'content',
        'category__title'
    ]


    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]