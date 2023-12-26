from django.urls import path
from bookshopapp import views
urlpatterns = [
    path('',views.base,name = "base"),
]