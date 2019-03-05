from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """"a model for blog post"""
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.title
