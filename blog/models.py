from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField(max_length= 2550)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    pub_date = models.DateTimeField(auto_now=False,auto_now_add=True)