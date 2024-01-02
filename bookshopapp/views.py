from django.shortcuts import render, redirect
from . forms import SignUpForm

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
        if form.is_valid():
            form.save()
            print(form.save())
            return redirect('base')
    else:
        form = SignUpForm
    return render(request,'bookshopapp/registerpage.html',{'form':form})