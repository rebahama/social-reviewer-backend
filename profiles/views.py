from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from social_drf.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializer import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Retrive the profiles and show how many likes a profile has.
        Users can also sort the profile based on how popular the profile
        is with the help of a like count.
        Users can search a profile with the help of a name
        or profile name """

    queryset = Profile.objects.annotate(review_counter=Count('owner__post',
                                        distinct=True),
                                        profile_like=Count('profile_likes',
                                        distinct=True)
                                        ).order_by('-created_at')

    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = [
        'review_counter',
        'profile_like'

    ]

    search_fields = [
        'owner__username',
        'name'

    ]

    filterset_fields = [
        'owner__post'

    ]


class ProfileListDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
