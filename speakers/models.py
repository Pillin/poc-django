from django.db import models

# Create your models here.


class Speaker(models.Model):
    name = models.CharField("Nombre", default="", max_length=200)
    twitter = models.CharField(
        "twitter", default="", max_length=200, blank=True)
    youtube = models.CharField(
        "youtube", default="", max_length=200, blank=True)
    twitch = models.CharField("twitch", default="",
                              max_length=200, blank=True)
    linkedin = models.CharField(
        "Linkedin", default="", blank=True, max_length=200)

    def __str__(self):
        return self.name
