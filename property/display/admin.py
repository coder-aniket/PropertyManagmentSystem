from django.contrib import admin
# from .models import Profile
from .user import Profile
from .property import Property,Feature
# Register your models here.
admin.site.register(Profile)
admin.site.register(Feature)