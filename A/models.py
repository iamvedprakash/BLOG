from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    thumb = models.ImageField(default='var.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:40] + "..."
