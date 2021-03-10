from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import User

# Create your views here.

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		if username is not '' and password is not '':
			if User.objects.filter(username=username).exists() and User.objects.filter(username=username).first().password == password:
				return redirect(reverse("weather:weather_info"))
			else:
				messages.error(request,"Username or password invalid")
				return render(request,"account/login.html")
		else:
			messages.error(request,"All fields must required")
			return render(request,"account/login.html")
	else:
		return render(request,"account/login.html")

def register(request):
    if request.method == "POST" :
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['repassword']
        #check the data is entered or not by the user
        if username != '' and password1 != '' and password2 != '':
            #check password and repassword are same or not
            if password1 == password2:
                #if both are same then forward procced
                if User.objects.filter(username = username).exists():
                    messages.error(request,'username already taken')
                    return render(request,'account/register.html')
                else :
                    user = User(username = username , password = password1)
                    user.save()
                    messages.info(request,"Account created please login here")
                    return redirect(reverse("account:login"))
                    
            #if passwords are not match then again render register pagr                               
            else:
                messages.error(request,"password does not match")
                return render(request,'account/register.html')
        else:
            messages.error(request,"all fields are must required")
            return render(request,'account/register.html')

    else:
         return render(request,'account/register.html')