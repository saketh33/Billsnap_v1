from django.shortcuts import render, redirect, get_object_or_404
import pandas
from .models import applists,customer,csvs
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

@login_required
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

@login_required
def showapps(request):
    appli=applists.objects.all()
    leni=len(appli)
    return render(request,'showapps.html',{'showapp':appli,'leni':leni})

@login_required
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
        utility_address=request.POST.get('utility_address')

        #contact details
        contact_person= request.POST.get('contact_person')
        contact_email = request.POST.get('contact_email')
        contact_phnum =request.POST.get('contact_phnum')
        contact_mobile=request.POST.get('contact_mobile')
        contact_designation= request.POST.get('contact_designation')
        contact_landline=request.POST.get('contact_landline')

        emergency_person=request.POST.get('emerg_person')
        emergency_altperson=request.POST.get('emerg_altperson')
        emergency_mobile=request.POST.get('emerg_mobile')
        emergency_altmobile=request.POST.get('emerg_altmobile')
        emergency_officeaddress=request.POST.get('emerg_officeaddress')
        emergency_altofficeaddress=request.POST.get('emerg_altofficeaddress')

        #contact details
        addcus.utility_name =utility_name
        addcus.utility_short_name = utility_short_name
        addcus.utility_state = utility_state
        addcus.utility_district = utility_district
        addcus.utility_country = utility_country
        addcus.utility_postalcode = utility_postalcode
        addcus.utility_address=utility_address

        addcus.contact_person = contact_person
        addcus.contact_email=contact_email
        addcus.contact_phnum=contact_phnum
        addcus.contact_mobile=contact_mobile
        addcus.contact_designation=contact_designation
        addcus.contact_landline=contact_landline

        addcus.emergency_person=emergency_person
        addcus.emergency_altperson=emergency_altperson
        addcus.emergency_mobile=emergency_mobile
        addcus.emergency_altmobile=emergency_altmobile
        addcus.emergency_officeaddress=emergency_officeaddress
        addcus.emergency_altofficeaddress=emergency_altofficeaddress

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

import pandas as pd
def bulk_upload(request):
    if request.method=='POST':
        csvfile=request.FILES.get('csvfile')

        df=pd.read_csv(csvfile)
        l=list(df.columns)
        if l==['LatD', ' "LatM"', ' "LatS"', ' "NS"', ' "LonD"', ' "LonM"', ' "LonS"', ' "EW"', ' "City"', ' "State"']:
            objs = [csvs(
                LatD= row['LatD'],
                LatM  = row[' "LatM"'],
                LatS= row[' "LatS"'],
                NS= row[' "NS"'],
                LonD  = row[' "LonD"'],
                LonM  = row[' "LonM"'],
                LonS  = row[' "LonS"'],
                EW  = row[' "EW"'],
                City  = row[' "City"'],
                State= row[' "State"']
                )
            for i,row in df.iterrows()]
            csvs.objects.bulk_create(objs)
            return redirect('uploadlist')
        else:
            status=0
            return render(request, 'bulkupload.html',{'stat':status})
    else:
        stat=00
        return render(request, 'bulkupload.html',{'stat':stat})

def uploadlis(request):
    cols=[f.name for f in csvs._meta.get_fields()]
    dets=csvs.objects.all()
    return render(request,'uploadlist.html',{'details':dets,'columns':cols})

def settings(request):
    if request.method=='POST':
        custlis=request.POST.get('custlis')