from django.contrib.auth.models import User
from core.models import Item, Category
from core.serializers import ItemSerializer, UserSerializer, CategorySerializer
from core.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions


class ItemList(generics.ListCreateAPIView):
    """
    restful_hummer/apidocjs/itemdocs.py
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    restful_hummer/apidocjs/itemdocs.py
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    restful_hummer/apidocjs/categorydocs.py
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
