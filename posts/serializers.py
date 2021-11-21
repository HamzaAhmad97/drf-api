from django.db.models import fields
from rest_framework import serializers

from .models import Post

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'hashtags', 'time_added', 'time_updated', 'notes')