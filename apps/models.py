from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
import hashlib
from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def get_unique_string(body, time):
    s = str(body)+str(time)
    result_str = hashlib.sha1(s.encode()).hexdigest()[:10]
    return result_str

class applists(models.Model):
    appname=models.CharField(verbose_name='App name',primary_key=True,max_length=50,unique=True,null=False)
    appimg=models.ImageField(upload_to = 'app_images',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='created date',auto_now_add=True,editable=False,null=True,blank=True)
    updated_at = models.DateTimeField(verbose_name='updated date',null=True,blank=True)
    slug = models.SlugField(max_length=255, null=True, unique=True, editable=False)

    def __str__(self):
        return str(self.appname)

    def save(self, *args, **kwargs):
        super(applists, self).save()
        self.slug = slugify(self.appname)
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

    def __str__(self):
        return self.utility_name

class csvs(models.Model):
    LatD=models.CharField(max_length=50, null=True, blank=True)
    LatM=models.CharField(max_length=50, null=True, blank=True)
    LatS=models.CharField(max_length=50, null=True, blank=True)
    NS=models.CharField(max_length=50, null=True, blank=True)
    LonD=models.CharField(max_length=50, null=True, blank=True)
    LonM=models.CharField(max_length=50, null=True, blank=True)
    LonS=models.CharField(max_length=50, null=True, blank=True)
    EW=models.CharField(max_length=50, null=True, blank=True)
    City=models.CharField(max_length=50, null=True, blank=True)
    State=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.State)

class settings(models.Model):
    custlis=models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.State)