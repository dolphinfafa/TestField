from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)

    event_date = models.DateField(null=True)

    event_des = models.TextField()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

# Create your models here.
