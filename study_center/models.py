from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class StudyCenter(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    manager = models.OneToOneField('study_center.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    location = models.TextField(max_length=1000, blank=True,null=True) #url
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name + " / " + self.address
    
    def save(self, *args, **kwargs):
        if self.manager:
            if not self.manager.is_manager:
                raise BaseException("Manager must be a manager")
        if self.location:
            self.latitude = self.location[self.location.index('@')+1 : self.location.index(',')]
            self.longitude = self.location[self.location.index(',')+1 : len(self.location[:self.location.index(',')+1])+self.location[self.location.index(',')+1:].index(',')]
            self.address = self.location[self.location.index('place/')+6 : len(self.location[:self.location.index('place/')+6])+self.location[self.location.index('place/')+6:].index('/')].replace('+', ' ').replace('%22', '"')
        if self.contact_number:
            if (len(self.contact_number) != 12 or not self.contact_number.isdigit()):
                raise BaseException("Phone number is wrong")
        super().save(*args, **kwargs)

class CustomUser(AbstractUser):
    active = models.BooleanField(default=True)
    full_name = models.CharField(max_length=255)
    photo = models.FileField(null=True, blank=True)
    phone_number = models.CharField(max_length=12)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name + " / " + self.phone_number
    
    def save(self, *args, **kwargs):
        if (len(self.phone_number) != 12 or not self.phone_number.isdigit) and self.phone_number:
            raise BaseException("Phone number is wrong")
        if len(self.password) < 8:
            raise BaseException("Password is too short")
        if self.password.isdigit():
            raise BaseException("Password is enitrely numeric")
        super().save(*args, **kwargs)
        
class SocialStatus(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=355)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Social statuses'

class Course(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    social_status = models.ForeignKey('study_center.SocialStatus', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name + " / " + str(self.social_status)

class Certificate(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=12, null=True, blank=True)
    gender = models.TextField(choices=models.TextChoices("genders", "male female unknown"), max_length=7, default="unknown")
    social_status = models.ForeignKey(SocialStatus, on_delete=models.SET_NULL, null=True, blank=True, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if (len(self.contact_number) != 12 or not self.contact_number.isdigit) and self.contact_number and len(self.contact_number)>0:
            raise BaseException("Phone number is wrong")
        super().save(*args, **kwargs)