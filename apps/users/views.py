from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from apps.blog.models import Blog


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
