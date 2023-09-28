
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('register', views.RegisterView.as_view(), name="register"),
]
