# import logging

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from voter.forms import LoginForm
# Create your views here.

# logger = logging.getLogger(__name__)


# Main page
class IndexView(View):
    template_name = 'voter/index.html'

    def get(self, request):
        return render(request, self.template_name)


# For logging in user
class LoginView(View):
    template_name = 'voter/login.html'
    login_form = LoginForm

    def get(self, request):
        form = self.login_form()
        return render(request, self.template_name, context={'login_form': form})

    def post(self, request):
        form = self.login_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('email'),
                                password=data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                pass
                # user does not exists or wrong data
        return render(request, self.template_name, context={'login_form': form})


# Simple logout, after that redirect to index page
def logout_view(request):
    logout(request)
    return redirect('index')


class ProfileView(LoginRequiredMixin, View):
    login_url = '/login'
    # redirect_field_name = 're'
    template_name = 'voter/profile.html'

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        print("NOT IMPLEMENTED PFORILE POST")
        pass