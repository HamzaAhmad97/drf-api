from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

from blog.settings import AUTH_PASSWORD_VALIDATORS
from django.contrib.auth import get_user_model

class Post(models.Model):
    hashtags_list = [
        ('art','art'),
        ('sports','sports'),
        ('science','science'),
        ('general','general'),
        ('community','community'),
        ('life','life')
    ]
    title = models.CharField(max_length=64)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    time_added = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    hashtags = models.CharField(max_length=9, choices=hashtags_list, default='life')
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    

