from django.db import models

# Create your models here.
class cakecookiez(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images')
    description=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

