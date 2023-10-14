from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField(max_length= 2550)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    pub_date = models.DateTimeField(auto_now=False,auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=670)