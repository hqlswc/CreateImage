# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class vminfo(models.Model):
    name = models.CharField(max_length=20)
    memory = models.IntegerField()
    cpu = models.IntegerField()
    status = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
