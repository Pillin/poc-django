from django.db import models

# Create your models here.


class Reconnaissance(models.Model):
    name = models.CharField("Nombre", max_length=200)
    survey_id = models.CharField("Encuesta User id", max_length=200)
    is_disabled = models.BooleanField(default=False)
    gender = models.CharField("Genero", max_length=200)
    email = models.EmailField("Email", max_length=200)
    country = models.CharField("Country", max_length=200)
    region = models.CharField("Region", max_length=200)
    seniority = models.CharField("Seniority", max_length=200)
    company = models.CharField("Compania", max_length=200)
    tendency_raw = models.CharField("Tendency", max_length=200)
    speakers_raw = models.CharField("Speakers", max_length=200)
    mode = models.CharField("Nombre", max_length=200)
    has_newsletter = models.BooleanField(
        "Nombre", default=True, max_length=200)
    submitted_at = models.DateField("Nombre", max_length=200)

    def __str__(self):
        return self.name
