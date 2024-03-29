from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    
