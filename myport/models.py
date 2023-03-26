from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)    
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.id)+" "+str(self.active)+' '+self.name+' '+self.subject



