from django.shortcuts import render, redirect
from . forms import SignUpForm , LoginForm
from . models import Userprofile
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from . models import Book
from . serializers import BookSerializer


# Create your views here.
def base(request):
    return render(request,'bookshopapp/base.html')

def loginpage(request):
    return render(request,'bookshopapp/loginpage.html')

def test(request):
    return render(request,'bookshopapp/test.html')

def registerpage(request):
    return render(request,'bookshopapp/registerpage.html')

def login_valid(request):
    return render(request, 'bookshopapp/login_valid.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = SignUpForm
    return render(request,'bookshopapp/registerpage.html',{'form':form})


def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Userprofile.objects.get(username=username, password=password)
            request.session['user_id'] = user.id  # Storing user ID in the session
            print(f"############:{user.id}")
            request.session['mailid'] = user.email
            return render(request, 'bookshopapp/loginpage.html', {'username': username})  # Redirect to base.html on success
        except Userprofile.DoesNotExist:
            return render(request, 'bookshopapp/base.html', {'error': 'Invalid username or password'})
    return render(request, 'bookshopapp/login_valid.html')



""" user_id = request.session.get('user_id')
use this to use the id in our different function

"""


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





