from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField()
    author = models.CharField(max_length=30)
    author_email = models.EmailField()
