from django.db import models
import datetime
# Create your models here.

class Contacto(models.Model):
    name = models.CharField(max_length=150)
    mail = models.EmailField(blank=True, max_length=254)
    subject = models.CharField(max_length=150)
    description = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.now, blank=True,null=True)


    def __str__(self):
        return self.name

class Subscription(models.Model):
    mail = models.EmailField(blank=True, max_length=254)
    created = models.DateTimeField(default=datetime.datetime.now, blank=True,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.id
