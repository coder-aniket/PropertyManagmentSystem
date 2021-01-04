from django.db import models
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
import os

p_choices = [('Apartment','Apartment'),('House','House'),('Office','Office'),('Land','Land')]   # property type choice
o_choices = [('For Rent','For Rent'),('For Sale','For Sale')]                                   # offer type choice
s_choices = [('Available','Available'),('Sold','Sold')]                                         # status choice

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    property_title = models.CharField(max_length=30,null=False)
    property_type = models.CharField(max_length=10,null=False,choices=p_choices)
    offer_type = models.CharField(max_length=25,choices=o_choices)
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
    status = models.CharField(max_length=10,default="Available",choices=s_choices)
    # buyer = models.ForeignKey(User, on_delete=models.RESTRICT)

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
    Swimming_Pool = models.BooleanField(default=False)
    # image = models.FileField(upload_to='display/images/')
    class Meta:
        verbose_name = 'Properties'
        verbose_name_plural ='Properties'

    def add_property(request,pid):
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

            # print(property_type)
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
            if request.POST.get('Swimming_Pool')=="on":
                Swimming_Pool = True
            else:
                Swimming_Pool = False
            # print(pid)
            if(pid):
                del_file = request.POST['delete_img'].split(' + ')
                f = Feature.objects.filter(id=pid)
                # print(f)
                f.update(user_id=request.user.id, property_title=property_title, property_type=property_type,
                offer_type=offer_type, city=city, zip_code=zip_code, neighborhood=neighborhood,
                street=street,
                bedrooms=bedrooms, bathrooms=bathrooms, property_size=property_size, year=year, price=price,
                location=location, details=details, contact=contact, Attic=Attic, Garden=Garden,
                Microwave=Microwave,
                Dishwasher=Dishwasher, Gym=Gym, Patio=Patio, Fireplace=Fireplace,
                High_ceilings=High_ceilings,
                Swimming_Pool=Swimming_Pool)
                f[0].refresh_from_db()
                imgtable.add_image(request, f[0])

                for delf in del_file:
                    if delf:
                        print(delf)
                        img=imgtable.objects.get(img=delf).delete()
                        print(img)
            else:
                f = Feature(user_id=request.user.id,property_title=property_title,property_type=property_type,
                          offer_type=offer_type,city=city,zip_code=zip_code,neighborhood=neighborhood,street=street,
                          bedrooms=bedrooms,bathrooms=bathrooms,property_size=property_size,year=year,price=price,
                          location=location,details=details,contact=contact,Attic=Attic,Garden=Garden,Microwave=Microwave,
                          Dishwasher=Dishwasher,Gym=Gym,Patio=Patio,Fireplace=Fireplace,High_ceilings=High_ceilings,
                          Swimming_Pool=Swimming_Pool)
                f.save()

                imgtable.add_image(request,f)

        response = redirect('my_property')
        return response


    def sold(request,pid):
        property = Feature.objects.get(id=pid)
        property.status="Sold"
        property.save()
        response = redirect('my_property')
        return response

class imgtable(models.Model):
    property = models.ForeignKey(Feature,on_delete=models.CASCADE)
    img = models.FileField(upload_to='images/')

    # def __str__(self):
    # #     print(self.property)
    #     return property

    def add_image(request,pid):
        for img in request.FILES.getlist('property_image'):
            i = imgtable(property=pid,img=img)
            i.save()
