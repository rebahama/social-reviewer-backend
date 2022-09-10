from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, permissions, filters
from social_drf.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializer import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Retrive the profiles and set the """

    queryset = Profile.objects.annotate(review_counter=Count('owner__post', distinct=True),
    profile_like=Count('profile_likes', distinct=True)
    ).order_by('-created_at')

    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_filed = [
        'review_counter',
        'profile_like'

    ]


class ProfileListDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
