from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name='get')
class AccountView(TemplateView):
    template_name = 'users/account.html'
