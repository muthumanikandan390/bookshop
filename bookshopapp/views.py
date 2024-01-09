from django.shortcuts import render, redirect
from . forms import SignUpForm , LoginForm
from . models import Userprofile
from django.contrib.auth import authenticate, login
from rest_framework import viewsets,status
from . models import Book , Cart , CartItem
from . serializers import BookSerializer,CartItemSerializer
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt



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
            request.session['user_id'] = user.id  
            # print(f"############:{user.id}")
            request.session['mailid'] = user.email
            return render(request, 'bookshopapp/loginpage.html', {'username': username})  
        except Userprofile.DoesNotExist:
            return render(request, 'bookshopapp/base.html', {'error': 'Invalid username or password'})
    return render(request, 'bookshopapp/login_valid.html')



"""

user_id = request.session.get('user_id')
use this to use the id in our different function

"""
@require_POST
@csrf_exempt 

def add_to_cart(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    try:
        user = UserProfile.objects.get(id = user_id)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    try:
        book_id = request.POST.get(book_id)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    pass



















































# class CartItemViewSet(viewsets.ViewSet):
#     def create(self, request):
#         user_id = request.session.get('user_id')
#         if not user_id:
#             return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             user = Userprofile.objects.get(id=user_id)
#         except Userprofile.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         cart, created = Cart.objects.get_or_create(user=user)

#         book_id = request.data.get('book_id')
#         if not book_id:
#             return Response({'error': 'Book ID is required'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             book = Book.objects.get(id=book_id)
#         except Book.DoesNotExist:
#             return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

#         request.data['cart'] = cart.id
#         request.data['book'] = book.id

#         serializer = CartItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Book added to cart'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





