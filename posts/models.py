from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    created_on=models.DateTimeField(default=timezone.now)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.title)
    
    def get_absolute_url(self):
        return reverse('posts:user_posts_detail', kwargs={'pk': self.pk})