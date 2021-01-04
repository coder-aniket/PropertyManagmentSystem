from django.shortcuts import render,redirect,HttpResponse
# from .user import Profile
# from django.contrib.auth.models import User
from .property import Feature,imgtable
from .enquiry import Enquiry
# Create your views here.
def index(request):
   from .user import Profile
   property = Feature.objects.all()
   profc = len(property)      # property count
   propc=len(Profile.objects.all())    # user count
   propsc = len(Feature.objects.filter(status="Sold"))   # sold property count
   porfbc = len(Profile.objects.filter(type="Broker"))   # brokers count

   property=property[:6]
   imgs = firstimage(property)

   if request.user.id:     # wishlist of user
      wishlist = Profile.objects.get(user=request.user.id).wishlist
      if wishlist:
         wishlist = [int(n) for n in wishlist.split()]
   else:
      wishlist = 0

   broker = Profile.objects.filter(type='Broker')[:8]

   statspannel = {'profc':profc,'propc':propc,'propsc':propsc,'profbc':porfbc}

   return render(request,'index.html',{'property':property,'img':imgs,'wid':wishlist,'stats':statspannel,'broker':broker})

def add_property(request):
   if request.user.id:
      return render(request,'add_property.html')
   response = redirect('index')
   return response

def edit_property(request,pid):     # pid is id of property for edit
   # print(pid)
   property = Feature.objects.get(id=pid)
   image = imgtable.objects.filter(property_id=pid)
   ids = []
   imgs = []
   # print(ids)
   count=0                       # images of property
   for i in image:
      imgs.append([count,i])
      count += 1
   # print(imgs)
   return render(request,'edit_property.html', {'property':property,'img':imgs,'pid':pid})

def my_property(request,nav=0,step=" "):
   if request.user.id:
      from .user import Profile
      if step == "prev":
         last = nav
         initial = nav - 1
      else:
         last = nav + 1
         initial = nav

      if request.method=='POST':
         property = Feature.objects.filter(user_id=request.user.id)
         property = filterby(request,property)
      else:
         property = Feature.objects.filter(user_id=request.user.id)[initial:last + 1]
      print(property)
      try:
         if property[1]:
            end = True
      except:
         end = False
      property = property[:1]
      wishlist = Profile.objects.get(user=request.user.id).wishlist
      wishlist = [int(n) for n in wishlist.split()]
      # print(wishlist)
      imgs = firstimage(property)
      pindex = {'initial': initial, 'last': last}
      return render(request,'my_property.html',{'property':property,'img':imgs,'wid':wishlist,
                                                'pindex':pindex,'end':end,'myproperty':True,'end':end})
   response = redirect('index')
   return response

def list(request,nav=0,step=" "):
   if request.method=='POST':
      property=Feature.objects.all().exclude(status="Sold")
      property = filterby(request,property)
   else:
      property = Feature.objects.all().exclude(status="Sold")

   if step == "prev":
      last = nav
      initial = nav-12
   else:
      last = nav+12
      initial = nav
   property  = property[initial:last+1]
   try:
      if property[12]:
         end = True
   except:
      end = False
   property = property[:12]
   print(end)
   imgs = firstimage(property)
   wishlist = 0
   if request.user.id:
      from .user import Profile
      wishlist = Profile.objects.get(user=request.user.id).wishlist
      wishlist = [int(n) for n in wishlist.split()]

   pindex = {'initial':initial,'last':last}

   return render(request,'list.html',{'property':property,'img':imgs,'wid':wishlist,'pindex':pindex,'end':end})

def list_details(request,pid,eid=0):
   property = Feature.objects.get(id=pid)
   # print(p)
   flist = []
   if property.Attic:
      flist.append('Attic')
   if property.Garden:
      flist.append('Garder')
   if property.Microwave:
      flist.append('Microwave')
   if property.Dishwasher:
      flist.append('Dishwasher')
   if property.Gym:
      flist.append('Gym')
   if property.Patio:
      flist.append('Patio')
   if property.Fireplace:
      flist.append('Fireplace')
   if property.High_ceilings:
      flist.append('High ceilings')
   if property.Swimming_Pool:
      flist.append('Swimming Pool')
   img = imgtable.objects.filter(property_id=pid)
   # print(len(img))
   image = []
   c = 0
   count = []
   for i in img:
      image.append([c,i])
      c+=1
      count.append(c)
   # print(image)
   # print(type(count))
   rp = Feature.objects.filter(city=property.city).exclude(id=property.id)[:4]
   # print(p.city)
   imgs = firstimage(rp)
   if eid:
      enquiry = Enquiry.objects.get(id=eid)
   else:
      enquiry = False
   # print(enquiry.name)
   return render(request,'list_detail.html',{'property':property,'flist':flist,'img':image,'count':count,
                                             'rp':rp,'imgs':imgs,'enquiry':enquiry})

def team(request):
   from .user import Profile
   profile = Profile.objects.filter(type='Broker')[:8]
   # print(profile)
   return render(request,'team.html', {'profile': profile})

def wishlist(request):
   from .user import Profile
   wid = []
   property = []
   imgs = []
   if request.user.id:
      wishlist = Profile.objects.get(user=request.user.id).wishlist
      if wishlist:
         wishlist = wishlist.split(" ")
         for wi in wishlist:
            wid.append(int(wi))
            property.append(Feature.objects.get(id=wi))
            imgs.append(imgtable.objects.filter(property=wi).first())
         print(imgs)
         return render(request,'wishlist.html',{'property':property,'wid':wid})
      return render(request,'wishlist.html')
   return redirect('index')


def contact(request):
   return render(request,'contact.html')

def broker(request):
   return render(request,'broker.html')

def profile(request):
   if request.user.id:
      from .user import Profile
      profile = Profile.objects.get(user=request.user.id)
      enquiry = []
      property = Feature.objects.filter(user=request.user.id)
      for pid in property:
         eqp = Enquiry.objects.filter(property_id=pid.id)
         if eqp:
            for eqpid in eqp:
               enquiry.append(eqpid)
      # print(enquiry)
      return render(request,'profile.html',{'profile':profile,'enquiry':enquiry})
   response = redirect('index')
   return response

# def admin(request):
#    return render(request,'admin.html')

def shifttobroker(request):
   from .user import Profile
   profile = Profile.objects.get(user=request.user.id)
   profile.type = 'Broker'
   profile.save()
   # print(profile.type)
   return redirect('profile')

def firstimage(property):
   image = imgtable.objects.all()
   ids = []
   imgs = []
   for p in property:  # properties
      if p.id not in ids:
         ids.append(p.id)
   # print(ids)
   for id in ids:  # first image for per id
      for i in image:
         if id == i.property_id:
            imgs.append(i)
            break
   return imgs


def filterby(request,property):
   if request.POST['offer_type'] != 'all':
      property = property.filter(offer_type=request.POST['offer_type'])
   if request.POST['city'] != 'all':
      property = property.filter(city=request.POST['city'])
   if request.POST['bedrooms'] != 'all':
      if request.POST['bedrooms'] == '3+':
         property = property.filter(bedrooms__gte=3)
      else:
         property = property.filter(bedrooms=request.POST['bedrooms'])
   if request.POST['sort'] != 'all':
      property = property.order_by(request.POST['sort'])
   if request.POST['property_type'] != 'all':
      property = property.filter(property_type=request.POST['property_type'])
      print(request.POST['property_type'])
   if request.POST['min_price'] != '':
      property = property.filter(price__gte=request.POST['min_price'])
   if request.POST['max_price'] != '':
      property = property.filter(price__lte=request.POST['max_price'])

   return property




from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin

def test(request):
   p = Feature.objects.all()[:2]
   return render(request,'test.html',{'property':p})

@xframe_options_exempt
def test2(request):
   enquiry = Enquiry.objects.all().filter(user_id=request.user.id)
   # print(enquiry[0].property_id.id)
   image = imgtable.objects.all()
   ids = []
   imgs = []
   for p in enquiry:  # properties
      if p.property_id not in ids:
         ids.append(p.property_id.id)
   # print(ids)
   for id in ids:  # first image for per id
      for i in image:
         if id == i.property_id:
            imgs.append(i)
            break
   # print(enquiry[0].property_id.id)
   # print(imgs[0])
   return render(request,'test2.html',{'enquiry':enquiry,'img':imgs})

def abc(request):
   return render(request,'test.html')