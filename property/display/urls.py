from django.contrib import admin
from django.urls import path
from . import views,user,property,enquiry
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('add_property/', views.add_property, name="add_property"),
    path('edit_property/<int:pid>/', views.edit_property, name="edit_property"),
    path('my_property/', views.my_property, name="my_property"),
    path('my_property/<int:nav>/<slug:step>/', views.my_property, name="my_property"),
    path('list/', views.list, name="list"),
    path('list/<int:nav>/<slug:step>/', views.list, name="list"),
    path('list_details/<int:pid>/', views.list_details, name="list_details"),
    path('list_details/<int:pid>/<int:eid>/', views.list_details, name="list_details"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact"),
    path('broker/', views.broker, name="broker"),
    path('register/', user.Profile.register, name="register"),
    path('login/', user.Profile.log_in, name="login"),
    path('logout/', user.Profile.log_out, name="logout"),
    path('resetpass/', user.Profile.res_pass, name="respass"),
    path('profile/', views.profile, name="profile"),
    path('shifttobroker/',views.shifttobroker,name="shifttobroker"),
    path('abc/',views.test2,name="enquiry"),
    path('addproperty/', property.Feature.add_property, name="addproperty"),
    path('addproperty/<int:pid>/', property.Feature.add_property, name="editroperty"),
    path('enquiry/<int:pid>', enquiry.Enquiry.enquiry, name="add_message"),
    path('sold/<int:pid>',property.Feature.sold,name='sold'),
    path('mwishlist/<int:pid>',user.Profile.mwishlist,name='addwishlist'),
    path('seen/<int:eid>/',enquiry.Enquiry.seen,name='seen_enquiry'),
    path('close/<int:eid>/',enquiry.Enquiry.close,name='close_enquiry'),
    path('wishlist/',views.wishlist,name='wishlist'),
    # path('admin/', views.admin, name="admin"),
    path('test/', views.test, name="test"),
    path('test2/', views.test2, name="test2"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
