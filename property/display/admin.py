from django.contrib import admin
from .user import Profile
from .property import Feature,imgtable
from .enquiry import Enquiry
class Enquerym(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name','email','contact','message','property_id','status']
    search_fields = ['name','email','contact','message']
    list_filter = ['status']
    # prepopulated_fields = {'name': ('name',)}
class Profilem(admin.ModelAdmin):
    list_display = ['user','contact','type']
    list_filter = ['type']
    search_fields = ['user','contact']

class Featurem(admin.ModelAdmin):
    list_display = ['property_title','property_type','offer_type','city','price','property_size',
                    'bedrooms','bathrooms','contact','status']
    list_filter = ['status','property_type','offer_type']
    search_fields = ['property_title','city']
class imgtablem(admin.ModelAdmin):
    list_display = ['property','img']
    search_fields = ['property']

# Register your models here.
admin.site.register(Profile,Profilem)
admin.site.register(Feature,Featurem)
admin.site.register(imgtable,imgtablem)
admin.site.register(Enquiry,Enquerym)