from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from social_drf.permissions import IsOwnerOrReadOnly
from .models import Comments
from .serializer import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """ For comments, only authorazied user can update and delete comments"""
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comments.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    
    ordering_filed = [
        'rating',
    ]

    filterset_fields = [
        'post'

    ]



class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
