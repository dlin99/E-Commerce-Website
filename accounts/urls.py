from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('password/', views.changePassword, name="change-password"),    

    path('', views.userPage, name="user-page"),  
    path('update/', views.userPageUpdate, name="user-page-update"),   

    path('orders/', views.userOrders, name="user-orders"),   
    path('orders/<int:pk>', views.userOrdersDetail, name="user-orders-detail"),   
]
