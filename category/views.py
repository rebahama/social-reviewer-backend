from rest_framework import generics, permissions
from .models import Category
from .serializer import CategorySerializer


class CategoryList(generics.ListAPIView):
    """ Setting the query to the Category model object,
        the permission class means that only users are authenticated
        the serializer class takes the imported category serializer
        to serialize the data for the view  """
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
