from django.db import models
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .property import Feature
# from .user import Profile

e_choices =[('Open','Open'),('Seen','Seen'),('Close','Close')]  # enquiry status choice

class Enquiry(models.Model):
    contact = models.IntegerField()
    email = models.EmailField(max_length=25)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    property_id = models.ForeignKey(Feature,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    message = models.TextField(max_length=500)
    status = models.CharField(max_length=10,default='Open',choices=e_choices)

    def __str__(self):
        return self.property_id.property_title

    def enquiry(request,pid):
        contact = request.POST['contact']
        email = request.POST['email']
        name = request.POST['name']
        message = request.POST['message']
        print(request.user.id)
        e=Enquiry(contact=contact,email=email,property_id = Feature.objects.get(id=pid),name=name,message=message)
        if request.user.id:
            e.user_id = User.objects.get(id=request.user.id)
        e.save()
        response = redirect('index')
        return response

    def seen(request,eid):
        enquiry = Enquiry.objects.get(id=eid)
        enquiry.status = "Seen"
        enquiry.save()
        return redirect('profile')

    def close(request,eid):
        enquiry = Enquiry.objects.get(id=eid)
        enquiry.status = "Close"
        enquiry.save()
        return redirect('profile')