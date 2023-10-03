
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
   return render(request, 'home.html')
   # return HttpResponse('hello')


def user_login(request):
   if request.method== 'POST':
      u_name= request.POST['username']
      u_pass= request.POST['password']
      user= authenticate(request, username=u_name, password= u_pass)
      print(u_name, u_pass)
      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         messages.error(request, 'Imvalid Email Id/Password')
         return render(request, 'login.html' )
   return render(request, 'login.html' )
   # return render(request, 'login.html')


class RegisterView(View):
   def get(self, request):
      return render(request, 'register.html')

   def post(self, request):
      fname= request.POST['fname']
      lname= request.POST['lname']
      uname= request.POST['email']
      password= request.POST['password']
      try:
         save_user= User.objects.create_user(first_name=fname, last_name=lname, username=uname, password= password)
         save_user.save()
         return redirect('user_login')
      except:
         return render(request, 'register.html')

   # return render(request, 'register.html')

def log_out(request):
   logout(request)
   return redirect('user_login')