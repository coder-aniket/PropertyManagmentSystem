from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from .models import Profile
from . import views
from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return User.objects.get(id=self.user_id).username

    def register(request):
        if request.method=="POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            contact=request.POST['contact']
            password=request.POST['password']
            us = User.objects.create_user(email,email,password,first_name=fname,last_name=lname)
            p=Profile(user=us,contact=contact)
            p.save()
        response = redirect('index')
        return response

    def log_in(request):
        email = request.POST['email']
        password = request.POST['password']
        us = authenticate(request, username=email, password=password)
        if us is not None:
            login(request,us)
            # Redirect to a success page.
            # print(request.user.username)
            response = redirect('index')
            return response
        else:
            return HttpResponse("failed")

    def log_out(request):
        logout(request)
        # Redirect to a success page.
        response = redirect('index')
        return response

    def res_pass(request):
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        try:
            id = User.objects.get(username=email).id
            pu_id = Profile.objects.filter(user_id=id,contact=contact)#.first()
            if pu_id:
                us = User.objects.get(id=pu_id[0].user_id)
                us.set_password(password)
                us.save()
                # Redirect to a success page.
                response = redirect('index')
                return response
        except User.DoesNotExist:
            return HttpResponse("failed");
        except Profile.DoesNotExist:
            return HttpResponse("failed");