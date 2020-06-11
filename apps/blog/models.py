from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )

    @property
    def posts(self):
        return BlogPost.objects.filter(blog=self)

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')

    def __str__(self):
        return _('%s\'s blog') % self.user.username


class BlogPost(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        verbose_name=_('blog'),
        related_query_name='posts',
        null=False,
    )
    title = models.CharField(_('post title'), max_length=255)
    text = models.TextField(_('post text'))
    date_created = models.DateTimeField(default=now)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-date_created']

    def __str__(self):
        return f'[{self.pk}] {self.title}'


@receiver(post_save, sender=get_user_model(), dispatch_uid='user.subscriptions.changed')
def user_post_save(instance, created, **kwargs):
    if created:
        Blog.objects.create(user=instance)


@receiver(post_save, sender=BlogPost, dispatch_uid='blog_post.save')
def blog_post_post_save(instance, created, **kwargs):
    """
    Here we do send email, to inform subscribed user new post has been published
    But to make this code works, we need to setup connection to SMTP server. 
    """
    if created:
        for user in instance.blog.subscribed_users.all():

            user.email_user(
                _('New post'),
                _('Here\'s a new post. Chech it out %(base)s%(url)s')
                % {
                    'base': settings.URL_FOR_EMAIL,
                    'url': reverse('blog-post-detail', kwargs={'pk': instance.pk}),
                },
                fail_silently=True,
            )
