
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.timezone import now


# Create your models here.

# User model

# Receipt Model

class Receipt (models.Model):
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    receipt_image=models.ImageField(upload_to='static/images')
    date_saved=models.DateTimeField(now())
