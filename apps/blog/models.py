from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name=_('blog'))
    title = models.CharField(_('post title'), max_length=255)
    text = models.TextField(_('post text'))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


@receiver(post_save, sender=get_user_model())
def user_post_create(instance, created, **kwargs):
    if created:
        Blog.objects.create(user=instance)
