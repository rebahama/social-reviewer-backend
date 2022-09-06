from django.shortcuts import render
from rest_framework import generics, permissions
from social_drf.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializer import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Retrive the profiles and set the """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]


class ProfileListDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
