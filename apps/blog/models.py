from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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
