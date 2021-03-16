from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound    

# import pdb; pdb.set_trace()

# username = "rediyus"
# print(f"Hi, {username}")

def home(request):
    return render(request, 'front/home.html')

def panel(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    return render(request, 'back/index.html')   #index.html=panel

def sign_up(request):
    if request.method == "GET":
        return render(request, "front/sign_up.html")
    elif request.method == "POST":
        email = request.POST.get("email")

        try:
            user = User.objects.get(username=email)

            messages.error(request, f"{email} already registered")

            return redirect("sign_up")
        except User.DoesNotExist:
            password = request.POST.get("password")
            confirmation_password = request.POST.get("confirmation_password")

            if password != confirmation_password:
                messages.error(request, "password mismatch")
                return redirect("sign_up")

            user = User.objects.create_user(username=email, email=email, password=password)
            user.save

            login(request, user)

            return redirect("panel")

    return HttpResponseNotFound  

#connecting from login html to django admin login start from here. 
def mylogin(request):

    if request.method == 'POST' :

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username != "" and password != "" :

            user = authenticate(username=username, password=password)

            if user is not None :
                breakpoint

                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')


def daftarkegiatan(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    return render(request, 'back/daftarkegiatan.html')   #index.html=panel

def stickynotes(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    return render(request, 'back/stickynotes.html')   #index.html=panel

def kalender(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    return render(request, 'back/kalender.html')   #index.html=panel