from django.shortcuts import render, redirect
from django.urls import reverse
from models import User_Wishlist, Others_Wishlist, NewList
from ..myLoginReg.views import print_messages
from ..myLoginReg.models import User


#from django.template import Library
#register = Library()

def check_logged_in(request):
    """
    Use this function to return whether or not the user is logged in
    """
    return 'user' in request.session


def index(request):
    if not check_logged_in(request):
        return redirect(reverse('users:index'))

    context = {
        'u_wishlist' : User_Wishlist.objects.all(),
        'o_wishlist' : Others_Wishlist.objects.all()
    }

    return render(request, 'myDashboard/index.html', context)

def new(request):
    if not check_logged_in(request):
        return redirect(reverse('users:index'))

    context = {
        'u_wishlist' : User_Wishlist.objects.all(),
        'o_wishlist' : Others_Wishlist.objects.all()
    }

    return render(request, 'myDashboard/new.html', context)

def create(request):
    if not check_logged_in(request):
        return redirect(reverse('users:index'))

    result = NewList.objects.create_list(request.POST, request.session['user']['id'])

    if result[0] == True:
        return redirect(reverse('dashboard:show', kwargs={'id': result[1].item.id }))
    else:
        print_messages(request, result[1])
        return redirect(reverse('dashboard:new'))


def show(request, id):
    if not check_logged_in(request):
        return redirect(reverse('users:index'))

    userlist = User_Wishlist.objects.get(id=id)
    return render(request, 'myDashboard/show.html', { 'userlist' : userlist })


def show_user(request, id):
    if not check_logged_in(request):
        return redirect(reverse('users:index'))

    user = User.objects.fetch_user_info(id)
    return render(request, 'myDashboard/show_user.html', { 'user' : user })
