from cv2 import illuminationChange
from django.db import models

# Create your models here.
import hashlib
from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
User._meta.get_field('email')._unique = True

def current_year():
        return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year()+10)(value)

def get_unique_string(body, time):
    s = str(body)+str(time)
    result_str = hashlib.sha1(s.encode()).hexdigest()[:10]
    return result_str

gender_choices = (('M', 'MALE'),
('F', 'FEMALE'),
('O', 'OTHER'))
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # personal details
    
    full_name               =       models.CharField(max_length=100, blank=True, null=True)
    state                   =       models.CharField(max_length=40, null=True, blank=True)
    city                    =       models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    ph_num = models.CharField(max_length=15, null=True, blank=True)
    xp = models.IntegerField(null=True, default=100, blank=True)
    techsnap_cash = models.IntegerField(null=True, default=999, blank=True)
    slug = models.SlugField(max_length=200, editable=False, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(Profile, self).save()
        self.slug = slugify(self.user.username)
        super(Profile, self).save()

    def courseprofile(self):
        return self.course_profile.all()

class Notifications(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_notifications')
    image = models.ImageField(upload_to='notifications')
    mark_as_read = models.BooleanField(default=False)
    body = models.TextField()
    url = models.URLField(null=True, blank=True)
    url_name = models.CharField(max_length=255, default='View', null=True, blank=True)
    notified_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=16, null=True, unique=True, editable=False)

    def __str__(self):
        return self.profile.user.username + ' ' + self.body[0:15]

    def save(self, *args, **kwargs):
        super(Notifications, self).save()
        self.slug = slugify(get_unique_string(self.body, self.notified_time))
        super(Notifications, self).save()

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

