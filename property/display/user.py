from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from . import views
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
p_choices = [('Broker','Broker'),('User','User')]   # user profile type choice
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    type = models.CharField(max_length=6,default=User,choices=p_choices)
    wishlist = models.CharField(max_length=150,null=True)

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

    def mwishlist(request,pid):
        profile = Profile.objects.get(user=request.user.id)
        # print(profile.wishlist)
        # print(pid)
        if profile.wishlist:
            list = profile.wishlist.split(" ")
            # print(list)
            # print(type(list[0]))

            for wpid in list:
                # print(type(wpid),wpid)
                if wpid==str(pid):
                    list.remove(wpid)
                    profile.wishlist=" ".join(list)
                    break
            else:
                profile.wishlist=profile.wishlist+" "+str(pid)
        else:
            profile.wishlist=str(pid)
        profile.save()
        return HttpResponse("")