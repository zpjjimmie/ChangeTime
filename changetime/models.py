# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class TimeDatas(models.Model):
	change_time = models.DateTimeField('Change')
	def is_early_time(self):
		now = timezone.now();
		return now >= self.change_time
