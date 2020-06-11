from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    subscriptions = models.ManyToManyField(
        'blog.Blog',
        related_name='subscribed_users',
        related_query_name='subscribed_users',
        blank=True,
    )

    @property
    def get_feed(self):
        from apps.blog.models import BlogPost

        return BlogPost.objects.filter(blog__in=self.subscriptions.all())


class UserFeedSeen(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(
        'blog.BlogPost', on_delete=models.CASCADE, related_name='seen'
    )
