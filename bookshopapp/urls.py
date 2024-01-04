from django.urls import path
from bookshopapp import views
urlpatterns = [
    path('',views.base,name = "base"),
    path('loginpage/',views.loginpage,name = "login-page"),
    path('test/',views.test,name = "test"),
    path('registerpage/',views.registerpage,name = "registerpage"),
    path('signup/',views.signup, name = "signup"),
    path('login_valid/',views.login_valid,name = 'login-valid'),
    path('login_auth/',views.login_auth,name = 'login-auth'),
    

]