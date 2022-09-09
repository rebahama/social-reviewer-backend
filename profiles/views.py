from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, permissions
from social_drf.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializer import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Retrive the profiles and set the """
    
    queryset = Profile.objects.annotate(review_counter=Count('owner__post', distinct=True)).order_by('-created_at')
    
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileListDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
