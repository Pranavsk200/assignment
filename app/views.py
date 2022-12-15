from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as dj_login,logout
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q

# Create your views here.

def adminUser(request):
    if request.user.is_superuser and request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            link = request.POST['link']
            category = request.POST['category']
            subCategory = request.POST['subCategory']
            points = request.POST['points']
            image = request.FILES.get('image')
            saveApp = App(appName = name, appLinks = link, appCategory = category, appSubCategory = subCategory, appPoints = points, appImage = image)
            saveApp.save()
            return redirect("adminHome")
        return render(request,"index.html")
    elif request.user.is_authenticated:
        user = request.user
        if Task.objects.filter(user=user).exists():
            apps = App.objects.filter(~Q(taskCompleted=user))         
            context = {
                'user':user,
                'app':apps
            }            
            return render(request,"UserFacing.html",context)              
        else:
            user=request.user
            apps = App.objects.all()
            context = {
                'user':user,
                'app': apps
            }
            return render(request,"UserFacing.html",context) 
    else:
        return redirect("login")           

def signin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['pass']
        repassword = request.POST['repass']
        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exists,please resistor with another username") 
                return redirect("signin")   
            else:    
                user =User.objects.create_user(username=username, password=password)
                user.save()
                print('user created')
                return redirect("login")
        else:
            messages.info(request, "conform passowerd and password are not matching")
    else:
        return render(request, "signin.html") 


def login(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['pass']
        user=authenticate(request, username=name, password=password)
        if user is not None:
            dj_login(request, user)
            current_user=request.user
            return redirect("home")
        else:
            #messages.success(request, "username or password is incorrect") 
            return redirect("login")   
    else:    
        return render(request,"login.html")

def logoutUser(request):
    if request.user.is_authenticated: 
        logout(request)
        return redirect("login") 
    else:
        return redirect("login")

def uploadScreenShort(request, id=None):
    if request.user.is_authenticated:
        if request.method =='POST':
            user = request.user
            app = App.objects.filter(id=id)[0]
            image = request.FILES.get('imagess')
            task =Task.objects.create(
                user = user, 
                app = app, 
                screenShort = image
            )
            app.taskCompleted.add(user)
            app.save()
            task.save()
            return redirect("home")
        app = App.objects.filter(id=id)[0]
        context = {
            'app':app
        } 
        return render(request, "uploadScreenshot.html", context)
    else:
        return redirect("login")    

def adminHome(request):
    if request.user.is_superuser and request.user.is_authenticated:
        app = App.objects.all()
        context = {
            'app':app
        }
        return render(request, 'adminHOME.html', context)
    else:
        return redirect("login")    

def userHome(request):
    if request.user.is_authenticated:
        user = request.user
        app = App.objects.filter(taskCompleted = user)
        context = {
            'app':app
        }
        return render(request, 'userHOME.html', context) 
    else:
        return redirect("login")        