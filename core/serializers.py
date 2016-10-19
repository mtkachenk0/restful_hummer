from rest_framework import serializers
from django.contrib.auth.models import User

from core.models import Category, Item


class ItemSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'categories', 'created', 'owner')


class CategorySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent_category', 'created', 'owner')


class UserSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'items', 'email', 'password')