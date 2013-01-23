from django.db import models

# Create your models here.

# a Script model contains mulitple Subtest models
class Script(models.Model):
    testname = models.CharField(max_length=100)

class Subtest(models.Model):
    subtestname = models.CharField(max_length=100)
    iterations = models.IntegerField()
    code = models.CharField(max_length=1000)

