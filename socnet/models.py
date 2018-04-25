from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=600, null=True)
    likes = models.ManyToManyField(User, blank=True)