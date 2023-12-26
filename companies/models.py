from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField("name", default="", max_length=200)

    def __str__(self):
        return self.name
