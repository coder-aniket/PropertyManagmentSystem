from django.shortcuts import render
from .property import Feature
# Create your views here.
def index(request):
   return render(request,'index.html')

def add_property(request):
   return render(request,'add_property.html')

def my_property(request):
   return render(request,'my_property.html')

def list(request):

   return render(request,'list.html')

def list_details(request):
   return render(request,'list_detail.html')

def team(request):
   return render(request,'team.html')

def contact(request):
   return render(request,'contact.html')

def broker(request):
   return render(request,'broker.html')

def profile(request):
   return render(request,'profile.html')

def admin(request):
   return render(request,'admin.html')

def test(request):
   proper = Feature.objects.all()
   context = {'property': proper}
   # print(p[2].bathrooms)
   return render(request,'test.html',context)