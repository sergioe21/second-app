from __future__ import unicode_literals

from django.db import models

# Create your models here.

class worker(models.Model):
	id_worker = models.AutoField
	last_name = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	age = models.IntegerField(default = 0)
	email = models.EmailField(max_length=100)

	def __str__(self):
		comp = self.first_name + ' ' +self.last_name
		return comp