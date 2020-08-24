from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os


# coderasha
# Create your views here.
@csrf_protect
def sign_up(request):
    # print(settings.LOGIN_URL)
    # print(os.getcwd())
    if request.method == 'POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user_name = form.cleaned_data.get('username')
            # pass_word = form.cleaned_data.get('password')
            # print (user_name, pass_word)
            # user = authenticate(username=user_name, password=pass_word)
            # login(request, user)
            # redirect(index)
    form = UserCreationForm()
    params = {'form':form}
    return render(request, 'loginapp/signup.html', params)

def index(request):
    return render(request, 'loginapp/index.html')

@csrf_protect    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            pass_word  = form.cleaned_data.get('password')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return redirect(index)
            else:
                return redirect(login)
        else:
            return redirect(login)
    else:
        form = AuthenticationForm()
    return render(request, 'loginapp/login.html', {'form':form})

@csrf_protect
def logout_request(request):
    logout(request)
    return redirect(index)

@csrf_protect
def signup_extra_fields(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username') 
            pass_word  = form.cleaned_data.get('password1') 
            user = authenticate(username=user_name, password=pass_word)
            login(request, user)
            return redirect(index)
    else:
        form = SignUpForm()
    return render(request, 'loginapp/signup.html', {'form':form})   

@login_required(login_url='../login/')
def home(request):
    return render(request, 'loginapp/index.html')







