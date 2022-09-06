from django.contrib import messages
from multiprocessing import context
from urllib.request import HTTPErrorProcessor
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import time
from datetime import datetime
from photographer.models import Contacts, Image

# Create your views here.
def index(request):
    # retrive uploaded image from user to home page
    images = Image.objects.all()
    context = {
        'Images': images
    }
    return render(request, 'index.html', context)
#-------------------------------------------------------------------------
def about(request):
    context = {
        "title": "About Page"
    }
    return render(request, 'about.html', context)
# -------------------------------------contact page form -------------------------------------------------- #
def contact(request):
    context = { "title": "Contact Page" }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pho_num = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contacts(fullname=name, email=email, pho_number=pho_num, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Contact Data Has been Submitted Successfully")
    return render(request, 'contact.html', context)

# -----------------------------------------------------

def handleSignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        try:
            user = User.objects.create_user(username, email, pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Your account has been successfully created")
            return redirect("/")
        except:
            messages.success(request, "This username has been taken please try another")
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
#-------------------------------------------------------------------------------------------

def loginUser(request): #retrive form data
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Your account has been successfully logged in!!")
            return redirect('/')
        else:
            messages.success(request, "Invalid username or password")
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")
# ---------------------------------------------------------------- 
def uplaod_images(request):
    if request.method == "POST" and request.FILES:
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES['image']
        desc = request.POST.get('desc')
        uplo_img = Image(fullname=name, email=email, desc=desc, date= datetime.today(), image=image, time = datetime.now())
        uplo_img.save()
        messages.success(request, 'Your photo has been successfully uploaded')
        
    return render(request, 'upload.html')