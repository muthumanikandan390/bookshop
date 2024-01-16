from django.shortcuts import render, redirect
from . forms import SignUpForm , LoginForm
from . models import Userprofile
from django.contrib.auth import authenticate, login
from rest_framework import viewsets,status
from . models import Book , Cart , CartItem , PurchasedItem
from . serializers import BookSerializer,CartItemSerializer,CartSerializer,BookNameSerializer
from rest_framework.response import Response
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.db import connection
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db import transaction



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

def purchase_page(request):
    return render(request, 'bookshopapp/purchasepage.html')

def loginpage_redirect(request):
    return render(request, 'bookshopapp/loginpage.html')


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


"""



@require_POST
@csrf_exempt 

def add_to_cart(request):
    try:
        data = json.loads(request.body)
        book_id = data.get('book_id')
       
        user_id = request.session.get('user_id')
        print(f"################### book id:{user_id}")
        if not user_id:
            return JsonResponse({"error": "User not logged in"}, status=403)
        try:
            user_profile = Userprofile.objects.get(id = user_id)
        except Userprofile.DoesNotExist:
            return JsonResponse({"error":"data not available"}, status = 404)

        #checking users cart

        try:
            cart = Cart.objects.get(user = user_profile)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user = user_profile)

        try:
            book = Book.objects.get(book_id = book_id)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)

        #checking book excistence

        cart_item_exists = CartItem.objects.filter(cart=cart, book=book).exists()

        if not cart_item_exists:
            CartItem.objects.create(cart=cart, book=book, quantity=1)
        
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT COUNT (*) FROM bookshopapp_cartitem WHERE cart_id = {cart.id}")
            row = cursor.fetchone()
        cart_item_count = row[0] if row else 0
        print(f"$$$$$$$$$$$ item count = {cart_item_count}")

        # cart_item_count = cart.items.count()
        # print(f"$$$$$$$$$$$ item count = {cart_item_count}")

        return JsonResponse({"message": "Book added to cart", "cartItemCount": cart_items_count})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookPopulateView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        print(f"user id ***********:{user_id}")
        if not user_id:
            return Response({'user not found'},status = 419)
        try:
            #user_profile = Userprofile.objects.get(id=user_id)
            books = Book.objects.all()
            serializer = BookNameSerializer(books, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CartItemViewSet(viewsets.ModelViewSet):
    pass

class CartDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if not user_id:
            return Response({"error": "User not logged in"}, status=403)
        try:
            cart = Cart.objects.get(user_id=user_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=404)

@api_view(['GET'])
def get_cart_item_count(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return Response({"error": "User not logged in"}, status=403)

    try:
        user_profile = Userprofile.objects.get(id=user_id)
        cart = Cart.objects.get(user=user_profile)
    except (Userprofile.DoesNotExist, Cart.DoesNotExist):
        return Response({"error": "Cart not found"}, status=404)

    cart_item_count = cart.items.count()
    return Response({"cartItemCount": cart_item_count})


class PurchasePageAPI(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if not user_id:
            return Response ('failed user', status = 409)
        try:
            cart = Cart.objects.get(user_id = user_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=404)


class purchased_item_api(APIView):
    def get(self,request,*args,**kwargs):
        user_id = request.session.get('user_id')
        if not user_id:
            return Response({'user not found'},status = 419)
        
        try:
            user = Userprofile.objects.get(id = user_id)
            cart = Cart.objects.get(user = user)

            cart_items = cart.items.all()

            if len(cart_items) == 0:
                return Response({'error': 'Cart is empty'}, status=400)
            
            with transaction.atomic():
                for item in cart_items:
                    PurchasedItem.objects.create(
                        user=user,
                        book=item.book,
                       
                    )
                cart_items.delete()
                return Response({'message':'Checkout successful'}, status=200)
        except Userprofile.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

                   
             
                   
                   
            


            


            





    














































class BookUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.session.get('user_id')
        print(f"user id ***********:{user_id}")
        if not user_id:
            return Response({'user not found'},status = 419)
        try:
            user_profile = Userprofile.objects.get(id=user_id)
            

            purchased_book_id = PurchasedItem.objects.filter(
                user = user_profile
                ).values_list('book', flat=True)
            print(f"the purchases are : { purchased_book_id }")

            books = Book.objects.exclude(id__in = purchased_book_id)

            serializer = BookNameSerializer(books, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



