from django.urls import path
from .views import PostsAPIView, PostDetailView

urlpatterns = [
    path('',PostsAPIView.as_view(), name='api_main'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_details')
]
