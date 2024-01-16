from django.urls import path,include
from rest_framework.routers import DefaultRouter

from bookshopapp import views
from bookshopapp.views import BookViewSet,CartDetailsView,get_cart_item_count,PurchasePageAPI,purchased_item_api,BookPopulateView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [ 
    path('',views.base,name = "base"),
    path('loginpage/',views.loginpage,name = "login-page"),
    path('test/',views.test,name = "test"),
    path('registerpage/',views.registerpage,name = "registerpage"),
    path('signup/',views.signup, name = "signup"),
    path('login_valid/',views.login_valid,name = 'login-valid'),
    path('login_auth/',views.login_auth,name = 'login-auth'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('purchase_page/',views.purchase_page,name = 'purchase-page'),
    path('loginpage_redirect/',views.loginpage_redirect,name = 'loginpage-redirect'),
    path('api/',include(router.urls)),
    path('api/cart/', CartDetailsView.as_view(), name='cart-details'),
    path('api/cart_item_count/', get_cart_item_count, name='cart_item_count'),
    path('purchase/', PurchasePageAPI.as_view(), name='purchase-page-api'),
    path('checkout/', purchased_item_api.as_view(), name='checkout'),
    path('bookpopulate/', BookPopulateView.as_view(), name='bookpopulate'),
    
    
]