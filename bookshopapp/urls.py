from django.urls import path
from bookshopapp import views
urlpatterns = [
    path('',views.base,name = "base"),
    path('loginpage/',views.loginpage,name = "login-page"),
    path('test/',views.test,name = "test"),
    path('registerpage/',views.registerpage,name = "registerpage"),

]