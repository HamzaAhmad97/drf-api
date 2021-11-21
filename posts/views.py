from rest_framework import generics
from .serializers import PostsSerializer
from .models import Post

class PostsAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

