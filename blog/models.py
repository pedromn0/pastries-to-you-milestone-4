from django.db import models
from django.utils import timezone

from profiles.models import UserProfile

# Create your models here.


class Post(models.Model):
    """
    Model responsabile to deal with post
    """

    title = models.CharField(max_length=160)
    slug = models.SlugField()
    intro = models.TextField()
    post_article = models.TextField()
    post_date_stamp = models.DateTimeField(default=timezone.now)
    post_user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        """
        Orderning the post by time
        """
        ordering = ['-post_date_stamp']


class Comments(models.Model):
    """
    Model responsabile to deal with commments
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comments_article = models.TextField(max_length=500)
    comments_date_stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comments_article

    class Meta:
        """
        Orderning the post by time
        """
        ordering = ['comments_date_stamp']
