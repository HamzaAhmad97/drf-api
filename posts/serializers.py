from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

class PostsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    class Meta:
        model = Post
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class NewPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(many = False)

    class Meta:
        model = Post
        fields = "__all__"