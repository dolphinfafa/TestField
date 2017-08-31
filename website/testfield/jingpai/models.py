from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)
    date = models.DateField(null=True)
    des = models.TextField()

    img = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

# Create your models here.
