from django.shortcuts import render, redirect, get_object_or_404
from .models import applists,customer
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def addapp(request):
    applis= applists()
    if request.method=='POST':
        app_name = request.POST.get('app_name')
        app_im= request.FILES.get('app_im')
        last_date= datetime.now()

        applis.appname=app_name
        applis.appimg= app_im
        applis.updated_at=last_date
        applis.save()
        return redirect('showapps')
    else:
        return render(request, 'applist.html')

def showapps(request):
    appli=applists.objects.all()
    return render(request,'showapps.html',{'showapp':appli})

def deleteapp(request,appname):
    deli=applists.objects.get(appname=appname)
    deli.delete()
    return redirect('showapps')



def addcustomer(request):
    addcus=customer()
    if request.method=='POST':

        utility_name = request.POST.get('utility_name')
        utility_short_name= request.POST.get('utility_short_name')
        utility_state= request.POST.get('utility_state')
        utility_district= request.POST.get('utility_district')
        utility_country=request.POST.get('utility_country')
        utility_postalcode= request.POST.get('utility_postalcode')
        #contact details
        contact_person= request.POST.get('contact_person')
        contact_email = request.POST.get('contact_email')
        contact_phnum =request.POST.get('contact_phnum')
        contact_designation= request.POST.get('contact_designation')
        office_address=request.POST.get('office_address')

        #contact details
        addcus.utility_name =utility_name
        addcus.utility_short_name = utility_short_name
        addcus.utility_state = utility_state
        addcus.utility_district = utility_district
        addcus.utility_country = utility_country
        addcus.utility_postalcode = utility_postalcode
        addcus.contact_person = contact_person
        addcus.contact_email=contact_email
        addcus.contact_phnum=contact_phnum
        addcus.contact_designation=contact_designation
        addcus.office_address=office_address

        addcus.save()
        return redirect('customerlist')
    else:
        return render(request, 'addcustomer.html')


def customerlis(request):
    cols=[f.name for f in customer._meta.get_fields()]
    dets=customer.objects.all()
    return render(request,'customerlist.html',{'details':dets,'columns':cols})

    #return render(request,'customerlist.html',{'data':zip(dets,cols)})

def deletecust(request,utility_name):
    deli=customer.objects.get(utility_name=utility_name)
    deli.delete()
    return redirect('customerlist')

from django.template import loader, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

def updaterecord(request,id):
    inst=customer.objects.get(id=id)
    if request.method=='POST':
        utility_name = request.POST.get('utility_name')
        utility_short_name= request.POST.get('utility_short_name')
        utility_state= request.POST.get('utility_state')
        utility_district= request.POST.get('utility_district')
        utility_country=request.POST.get('utility_country')
        utility_postalcode= request.POST.get('utility_postalcode')
        #contact details
        contact_person= request.POST.get('contact_person')
        contact_email = request.POST.get('contact_email')
        contact_phnum =request.POST.get('contact_phnum')
        contact_designation= request.POST.get('contact_designation')
        office_address=request.POST.get('office_address')

        instance=customer.objects.get(id=id)
        #contact details
        instance.utility_name =utility_name
        instance.utility_short_name = utility_short_name
        instance.utility_state = utility_state
        instance.utility_district = utility_district
        instance.utility_country = utility_country
        instance.utility_postalcode = utility_postalcode
        instance.contact_person = contact_person
        instance.contact_email=contact_email
        instance.contact_phnum=contact_phnum
        instance.contact_designation=contact_designation
        instance.office_address=office_address
        instance.save()

        return redirect('customerlist')
    else:
        return render(request, 'editcustomer.html',{'profile': inst})


'''class CustomerUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'customers.can_manage_customers'
    model = customer
    fields = [f.name for f in customer._meta.get_fields()]
    print(fields)'''
