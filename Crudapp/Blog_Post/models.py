from django.db import models
from datetime import datetime,date

# Create your models here.
class BlogPost(models.Model):
    date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    post=models.TextField(max_length=200)
    author=models.CharField(max_length=20)
    
    def __str__(self):
        return self.post