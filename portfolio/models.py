from django.db import models

# Create your models here.
class Audience(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' ' + self.email + ' ' + self.message