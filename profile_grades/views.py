from rest_framework import generics, permissions
from social_drf.permissions import IsOwnerOrReadOnly
from .models import ProfileLikes
from .serializer import ProfileLikeSerializer


class ProfileLikeList(generics.ListCreateAPIView):
    queryset = ProfileLikes.objects.all()
    serializer_class = ProfileLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileLikeDetail(generics.RetrieveDestroyAPIView):
    queryset = ProfileLikes.objects.all()
    serializer_class = ProfileLikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
