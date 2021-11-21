from rest_framework import serializers

from .models import Post

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','title', 'content', 'author', 'hashtags', 'time_added', 'time_updated', 'notes')