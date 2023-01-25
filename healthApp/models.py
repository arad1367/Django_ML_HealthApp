from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Symptom(models.Model): # It's better to define class name not plural
    def __str__(self) -> str:
        return self.firstname
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    sex = models.IntegerField(null=False, blank=False)
    cp = models.IntegerField(null=False, blank=False)
    trestbps = models.IntegerField(null=False, blank=False)
    chol = models.IntegerField(null=False, blank=False)
    fbs = models.IntegerField(null=False, blank=False)
    restecg = models.IntegerField(null=False, blank=False)
    thalach = models.IntegerField(null=False, blank=False)
    exang = models.IntegerField(null=False, blank=False)
    oldpeak = models.IntegerField(null=False, blank=False)
    slope = models.IntegerField(null=False, blank=False)
    ca = models.IntegerField(null=False, blank=False)
    thal = models.IntegerField(null=False, blank=False)