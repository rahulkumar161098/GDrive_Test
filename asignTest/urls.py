
from django.contrib import admin
from django.urls import path
from user import views
from bid import views as bidViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bidViews.getAllAuction, name="home"),
    path('user_login', views.user_login, name="user_login"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('details/<id>', bidViews.auctionDetail, name="auctionDetails"),
]
