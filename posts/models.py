from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    """
    A single blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title
