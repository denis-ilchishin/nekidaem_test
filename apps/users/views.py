from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, TemplateView

from apps.blog.models import Blog, BlogPost

from .models import UserFeedSeen


@method_decorator(login_required, name='get')
class AccountView(TemplateView):
    template_name = 'users/account.html'


@method_decorator(login_required, name='post')
class SubscribeView(View):
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk')
        blog = get_object_or_404(Blog, pk=pk)
        request.user.subscriptions.add(blog)
        return HttpResponseRedirect(reverse('blog-list'))


@method_decorator(login_required, name='post')
class UnsubscribeView(View):
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk')
        blog = get_object_or_404(Blog, pk=pk)
        request.user.subscriptions.remove(blog)
        return HttpResponseRedirect(reverse('blog-list'))


@method_decorator(login_required, name='post')
class MarkAsSeen(View):
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk')
        blog_post = get_object_or_404(BlogPost, pk=pk)
        user_feed_seen, new = UserFeedSeen.objects.get_or_create(
            user=request.user, post=blog_post
        )
        return HttpResponseRedirect(reverse('account'))


@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class PostCreateView(CreateView):

    model = BlogPost
    fields = (
        'title',
        'text',
    )

    def form_valid(self, form):
        form.instance.blog = self.request.user.blog
        self.success_url = reverse(
            'blog-detail', kwargs={'pk': self.request.user.blog.pk}
        )
        return super().form_valid(form)
