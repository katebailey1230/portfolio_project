from django.db import models

class Contact(models.Model):
    image = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=200)
