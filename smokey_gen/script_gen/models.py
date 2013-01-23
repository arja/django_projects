from django.db import models
from django import forms

# Create your models here.

# a Script model contains mulitple Subtest models
class Script(models.Model):
    testname = models.CharField(max_length=100)

class Subtest(models.Model):
    subtestname = models.CharField(max_length=100)
    iterations = models.CharField(max_length=100)
    code = models.CharField(max_length=10000)

class SubtestForm(forms.Form):
    name = forms.CharField(max_length=1000)
    body = forms.CharField()
    iterations = forms.CharField()
