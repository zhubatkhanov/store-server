from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)

def register(request):
    return render(request, 'users/register.html')
