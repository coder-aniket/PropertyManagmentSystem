from django.contrib import admin
from django.urls import path
from . import views,user,property
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('add_property/', views.add_property, name="add_property"),
    path('my_property/', views.my_property, name="my_property"),
    path('list/', views.list, name="list"),
    path('list_details/', views.list_details, name="list_details"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
    path('broker/', views.broker, name="broker"),
    path('register/', user.Profile.register, name="register"),
    path('login/', user.Profile.log_in, name="login"),
    path('logout/', user.Profile.log_out, name="logout"),
    path('resetpass/', user.Profile.res_pass, name="respass"),
    path('profile/', views.profile, name="profile"),

    path('addproperty/', property.Feature.add_property, name="addproperty"),

    path('admin/', views.admin, name="admin"),
    path('test/', views.test, name="test"),
]
