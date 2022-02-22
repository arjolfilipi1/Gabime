from django.db import models


class Per(models.Model):
    cir = models.CharField(max_length=200)
    grup = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    start_r = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    end_r = models.CharField(max_length=200)


class Op(models.Model):
    num = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    eq = models.CharField(max_length=4)


class Gab(models.Model):
    cir = models.CharField(max_length=200)
    grup = models.CharField(max_length=200)
    pos = models.CharField(max_length=200)
    cd = models.DateTimeField(auto_now=True)
    defect_code = models.CharField(max_length=30)
    lider_assy = models.CharField(max_length=200)
    lider_sub = models.CharField(max_length=200)
    masa = models.CharField(max_length=200)


class Opt(models.Model):
    con = models.CharField(max_length=200)
