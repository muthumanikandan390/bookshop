from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'bookshopapp/base.html')

def loginpage(request):
    return render(request,'bookshopapp/loginpage.html')

def test(request):
    return render(request,'bookshopapp/test.html')

def registerpage(request):
    return render(request,'bookshopapp/registerpage.html')