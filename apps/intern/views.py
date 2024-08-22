from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from apps.intern.forms import UserForm, UserLoginForm
from apps.intern.models import User


# Create your views here.
def index(request):
    return HttpResponse('Hello World')


class Signup(CreateView):
    model = User
    template_name = 'auth/register.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)




class Login(View):
    template_name = 'auth/login.html'
    form_class = UserLoginForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        print(email)
        print(password)
        print(user.email)
        if user is not None:
            print("Enter User")
            authenticated_user = authenticate(request, email=user.email, password=password)
            print(authenticated_user)
            if authenticated_user is not None:
                login(request, authenticated_user)
                context = {
                    'user_email': authenticated_user.email,
                    'user_first_name': authenticated_user.first_name,
                    'user_last_name': authenticated_user.last_name,
                }
                return render(request, 'dashboard.html', context)
            else:
                messages.error(request, 'Authentication failed. Please check your credentials.')
        else:
            print("Invalid Credentials")
            messages.error(request, 'User with this email does not exist.')

        return render(request, self.template_name, {'form': self.form_class})


class DashBoardView(TemplateView):
    template_name = 'layouts/dashboard.html'


def logout_view(request):
    logout(request)
    return redirect('login')
