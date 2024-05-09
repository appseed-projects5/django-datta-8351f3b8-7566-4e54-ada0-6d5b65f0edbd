# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Undefined(models.Model):

    #__Undefined_FIELDS__

    #__Undefined_FIELDS__END

    class Meta:
        verbose_name        = _("Undefined")
        verbose_name_plural = _("Undefined")


class Empresa(models.Model):

    #__Empresa_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Empresa_FIELDS__END

    class Meta:
        verbose_name        = _("Empresa")
        verbose_name_plural = _("Empresa")


class Nc_Inmueble(models.Model):

    #__Nc_Inmueble_FIELDS__
    nc = models.CharField(max_length=255, null=True, blank=True)

    #__Nc_Inmueble_FIELDS__END

    class Meta:
        verbose_name        = _("Nc_Inmueble")
        verbose_name_plural = _("Nc_Inmueble")


class Area(models.Model):

    #__Area_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Area_FIELDS__END

    class Meta:
        verbose_name        = _("Area")
        verbose_name_plural = _("Area")



#__MODELS__END
