from rest_framework import generics, permissions
from social_drf.permissions import IsOwnerOrReadOnly
from .models import ProfileLikes
from .serializer import ProfileLikeSerializer


class ProfileLikeList(generics.ListCreateAPIView):
    """ Give a profile a like"""
    queryset = ProfileLikes.objects.all()
    serializer_class = ProfileLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileLikeDetail(generics.RetrieveDestroyAPIView):
    """ Delete a profile like  """
    queryset = ProfileLikes.objects.all()
    serializer_class = ProfileLikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
