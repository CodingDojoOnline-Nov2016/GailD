from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    return render(request, 'myLoginReg/index.html')

def login(request):
    result = User.objects.validate_login(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('users:index'))
    return log_user_in(request, result[1])

def register(request):
    result = User.objects.validate_register(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('users:index'))
    return log_user_in(request, result[1])


def success(request):
    if not 'user' in request.session:
        return redirect(reverse('users:index'))
    #successful login, brings user to book reviews page
    return redirect(reverse('dashboard:index'))

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request, user):
    request.session['user'] = {
        'id' : user.id,
        'name' : user.name,
        'username' : user.username,        
    }
    return redirect(reverse('users:success'))

def logout(request):
    request.session.pop('user')
    return redirect(reverse('users:index'))
