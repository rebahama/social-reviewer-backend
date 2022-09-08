from rest_framework import generics, permissions
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



class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]