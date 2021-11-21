from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .serializers import NewPostSerializer, PostsSerializer
from .models import Post

class PostsAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = NewPostSerializer(queryset, many = True)
        return Response(serializer.data)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer