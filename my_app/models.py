
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
django.setup()
from django.db import models

# Create your models here.


class Line(models.Model):
    text = models.CharField(max_length=255)
