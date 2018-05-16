
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, login, LogoutView
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView

from user.models import Client


class IndexView(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    template_name = 'signup.html'
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST
        d = {}
        for key, value in data.items():
            d[key] = value


        del d['csrfmiddlewaretoken']
        del d['confirm_password']
        # d['username'] = d['email']
        if User.objects.filter(username= d['username']).count() or User.objects.filter(email=d['email']).count():
            error_data = {
                'error': 'Username or Email is already in use'
            }
            return render(request, self.template_name, context=error_data)
        else:
            user = Client.objects.create(**d)
            success = {
                'success': 'Successfully registered'
            }
            # email = EmailMessage(
            #             'hiii' , 'Please confirm', to=[d['username']]
            # )
            # email.send()
            return render(request, self.template_name, context=success)


class ClientLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/companies'

@method_decorator(login_required, name='dispatch')
class ClientDetail(DetailView):
    model = Client
    template_name = 'user_profile.html'
    context_object_name = 'client'
    queryset = Client.objects.all()


class ClientLogoutView(LogoutView):

    def get_next_page(self):
        return '/client/login/'