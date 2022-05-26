from django.urls import path
from . import views
from django.contrib.auth import views as a_views

urlpatterns = [
    path('addapp', views.addapp, name='addapp'),
    path('showapps', views.showapps, name='showapps'),
    path('deleteapp/<appname>',views.deleteapp,name='deleteapp'),
    path('customerlist',views.customerlis,name='customerlist'),
    path('addcust', views.addcustomer, name='addcust'),
    path('deletecustomer/<utility_name>',views.deletecust,name='deletecustomer'),
    path('update/<int:id>', views.updaterecord, name='updaterecord'),
    path('bulkupload', views.bulk_upload, name='bulkupload'),
    path('uploadlist', views.uploadlis, name='uploadlist'),
]