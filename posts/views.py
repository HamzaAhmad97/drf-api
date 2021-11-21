from rest_framework import generics
from .models import Post
from .serializers import PostsSerializer

class PostsAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

