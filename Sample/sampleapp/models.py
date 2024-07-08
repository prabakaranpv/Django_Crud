from django.db import models

# Create your models here.

class Mymodel(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Password = models.IntegerField()


    def __str__(self):
        return self.Name
