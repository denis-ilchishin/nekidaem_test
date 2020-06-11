from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth.views import LogoutView as DefaultLogoutView
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView


class HomeView(RedirectView):
    pattern_name = 'blog-list'


class LoginView(DefaultLoginView):
    template_name = 'login.html'


@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class LogoutView(DefaultLogoutView):
    pass
