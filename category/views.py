from rest_framework import generics, permissions
from .models import Category
from .serializer import CategorySerializer


class CategoryList(generics.ListAPIView):

    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer

