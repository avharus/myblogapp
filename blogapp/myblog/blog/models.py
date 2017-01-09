from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-date"]

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.text
