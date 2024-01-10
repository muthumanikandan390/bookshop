from django.urls import path,include
from rest_framework.routers import DefaultRouter

from bookshopapp import views
from bookshopapp.views import BookViewSet

router = DefaultRouter()
router.register('books',BookViewSet)


urlpatterns = [ 
    path('',views.base,name = "base"),
    path('loginpage/',views.loginpage,name = "login-page"),
    path('test/',views.test,name = "test"),
    path('registerpage/',views.registerpage,name = "registerpage"),
    path('signup/',views.signup, name = "signup"),
    path('login_valid/',views.login_valid,name = 'login-valid'),
    path('login_auth/',views.login_auth,name = 'login-auth'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('api/',include(router.urls)),
    
    

]