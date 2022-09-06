from django.db import models

# Create your models here.
class Contacts(models.Model):
    fullname = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=140)
    pho_number = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.fullname
    
class Image(models.Model):
    fullname = models.CharField(blank=True, max_length=255 , null=True)
    email = models.CharField(blank=True, max_length=140, null=True)
    image = models.ImageField(blank=True, null=True, upload_to = 'images/') #media/
    desc = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.fullname