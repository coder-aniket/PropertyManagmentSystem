from django.db import models
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
import os
class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_title = models.CharField(max_length=30,null=False)
    property_type = models.CharField(max_length=10,null=False)
    offer_type = models.CharField(max_length=25)
    city = models.CharField(max_length=15,null=False)
    zip_code = models.IntegerField(null=False)
    neighborhood = models.CharField(max_length=25,null=False)
    street = models.CharField(max_length=15,null=False)
    bedrooms = models.SmallIntegerField(null=False)
    bathrooms = models.SmallIntegerField(null=False)
    property_size = models.SmallIntegerField(null=False)
    year = models.IntegerField(null=False,default=2020)
    price = models.IntegerField()
    location = models.CharField(max_length=15,null=False)
    details = models.TextField()
    contact = models.IntegerField(null=True)

    def __str__(self):
        return self.property_title


class Feature(Property):
    # property = models.OneToOneField(Property,on_delete=models.CASCADE)
    Attic = models.BooleanField(default=False)
    Garden = models.BooleanField(default=False)
    Microwave = models.BooleanField(default=False)
    Dishwasher = models.BooleanField(default=False)
    Gym = models.BooleanField(default=False)
    Patio = models.BooleanField(default=False)
    Fireplace = models.BooleanField(default=False)
    High_ceilings = models.BooleanField(default=False)
    Swimmin_Pool = models.BooleanField(default=False)
    # image = models.FileField(upload_to='display/images/')


    def add_property(request):
        if request.method == "POST":
            property_title = request.POST['property_title']
            property_type = request.POST['property_type']
            offer_type = request.POST['offer_type']
            city = request.POST['city']
            zip_code = request.POST['zip_code']
            neighborhood = request.POST['neighborhood']
            street = request.POST['street']
            bedrooms = request.POST['bedrooms']
            bathrooms = request.POST['bathrooms']
            property_size = request.POST['property_size']
            year = request.POST['year']
            price = request.POST['price']
            location = request.POST['location']
            details = request.POST['details']
            contact = request.POST['contact']

            if request.POST.get('Attic')=="on":
                Attic = True
            else:
                Attic = False
            if request.POST.get('Garden') == "on":
                Garden = True
            else:
                Garden = False
            if request.POST.get('Microwave')=="on":
                Microwave = True
            else:
                Microwave = False
            if request.POST.get('Dishwasher')=="on":
                Dishwasher = True
            else:
                Dishwasher = False
            if request.POST.get('Gym')=="on":
                Gym = True
            else:
                Gym = False
            if request.POST.get('Patio')=="on":
                Patio = True
            else:
                Patio = False
            if request.POST.get('Fireplace') == "on":
                Fireplace = True
            else:
                Fireplace = False
            if request.POST.get('High_ceilings')=="on":
                High_ceilings = True
            else:
                High_ceilings = False
            if request.POST.get('Swimmin_Pool')=="on":
                Swimmin_Pool = True
            else:
                Swimmin_Pool = False

            f=Feature(user_id=request.user.id,property_title=property_title,property_type=property_type,
                      offer_type=offer_type,city=city,zip_code=zip_code,neighborhood=neighborhood,street=street,
                      bedrooms=bedrooms,bathrooms=bathrooms,property_size=property_size,year=year,price=price,
                      location=location,details=details,contact=contact,Attic=Attic,Garden=Garden,Microwave=Microwave,
                      Dishwasher=Dishwasher,Gym=Gym,Patio=Patio,Fireplace=Fireplace,High_ceilings=High_ceilings,
                      Swimmin_Pool=Swimmin_Pool)
            f.save()
            count=0
            image = request.FILES.getlist('property_image')
            os.mkdir("display/images/" + str(f.property_ptr_id))
            for i in range(len(image)):
                count = count + 1
                fil = open("display/images/"+str(f.property_ptr_id)+"/"+str(count)+".jpg",'wb+')
                fil.write(image[i].read())
                fil.close()


            response = redirect('index')
            return response
