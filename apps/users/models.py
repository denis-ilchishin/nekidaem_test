from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import m2m_changed


class User(AbstractUser):
    subscriptions = models.ManyToManyField(
        'blog.Blog',
        related_name='subscribed_users',
        related_query_name='subscribed_users',
        blank=True,
    )

    def get_feed(self):
        from apps.blog.models import BlogPost

        return BlogPost.objects.filter(blog__in=self.subscriptions.all()).annotate(
            seen=models.Exists(
                UserFeedSeen.objects.filter(user=self, post=models.OuterRef('pk')).only(
                    'pk'
                )
            )
        )


class UserFeedSeen(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='seen'
    )
    post = models.ForeignKey('blog.BlogPost', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'post'),)


def subscriptions_changed(instance, pk_set, action, **kwargs):

    if action == 'post_remove':
        user = instance
        removed = pk_set

        user.seen.filter(post__blog__in=removed).delete()


m2m_changed.connect(
    subscriptions_changed,
    sender=get_user_model().subscriptions.through,
    dispatch_uid='user.subscriptions.changed',
)
