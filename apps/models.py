from django.db import models
import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class applists(models.Model):
    appname=models.CharField(verbose_name='App name',primary_key=True,max_length=50,unique=True,null=False)
    appimg=models.ImageField(upload_to = 'app_images',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='created date',auto_now_add=True,editable=False,null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated date',null=True,blank=True)

    def __str__(self):
        return str(self.appname)

    def save(self, *args, **kwargs):
        super(applists, self).save()


class customer(models.Model):
    #utility details
    utility_name = models.CharField(max_length=200, null=True, blank=True)
    utility_short_name= models.CharField(max_length=50, null=True, blank=True)
    utility_state= models.CharField(max_length=50, null=True, blank=True)
    utility_district= models.CharField(max_length=50, null=True, blank=True)
    utility_country= models.CharField(max_length=50, null=True, blank=True)
    utility_postalcode= models.CharField(max_length=20, null=True, blank=True)

    #contact details
    contact_person= models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(max_length=50, null=True, blank=True)
    contact_phnum = models.CharField(max_length=15, null=True, blank=True)
    contact_designation= models.CharField(max_length=100, null=True, blank=True)
    office_address=models.TextField(max_length=200,null=True,blank=True)

    #contact details

    info_created_at = models.DateTimeField(auto_now_add=True)
    info_updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=16, null=True, unique=True, editable=False)


    def __str__(self):
        return self.utility_name
