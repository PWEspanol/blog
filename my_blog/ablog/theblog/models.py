from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    title_tag = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True, editable=False)
    is_featured = models.BooleanField(default=False, verbose_name="Featured Article")
    is_featured_header = models.BooleanField(default=False, verbose_name="Main Featured Article")
    trending = models.BooleanField(default=False, verbose_name="Trending")
    tags = TaggableManager()
    category = models.CharField(max_length=255)
    views= models.IntegerField(default=0)
    slug = models.SlugField(max_length=120, default="")
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')


    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # reply = models.ForeignKey('Comment', null=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content[:15]) + str(self.user.id)

