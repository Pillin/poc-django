from django.db import models

# Create your models here.


class Reconnaissance(models.Model):
    name = models.CharField("Nombre", default="", max_length=200)
    survey_id = models.CharField(
        "Encuesta User id",
        unique=True,
        default="",
        max_length=200
    )
    is_disabled = models.BooleanField(default=False)
    gender = models.CharField("Genero", default="", blank=True, max_length=200)
    email = models.EmailField("Email", default="", blank=True, max_length=200)
    country = models.CharField(
        "Country", default="", blank=True, max_length=200)
    region = models.CharField("Region", default="", blank=True, max_length=200)
    seniority = models.CharField(
        "Seniority", default="", blank=True, max_length=200)
    company_raw = models.CharField(
        "Compania",  default="", blank=True, max_length=200)
    tendency_raw = models.CharField(
        "Tendency", default="", blank=True, max_length=200)
    speakers_raw = models.CharField(
        "Speakers", default="", blank=True, max_length=400)
    speaker = models.ManyToManyField("speakers.Speaker", blank=True)
    mode = models.CharField("Mode", default="", max_length=200)
    has_newsletter = models.BooleanField(
        "Newsletter", default=True, max_length=200)
    submitted_at = models.DateField(
        "Submit", auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
