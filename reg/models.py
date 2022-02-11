from django.db import models


class Per(models.Model):
    cir = models.CharField(max_length=200)
    grup = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    start_r = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    end_r = models.CharField(max_length=200)


class Gab(models.Model):
    cir = models.CharField(max_length=200)
    grup = models.CharField(max_length=200)
    pos = models.CharField(max_length=200)
    cd = models.DateTimeField(auto_now=True)


class Opt(models.Model):
    con = models.CharField(max_length=200)
