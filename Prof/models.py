from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Counter(models.Model):

	
	cnt = models.IntegerField(default=0)

class Worker(models.Model):

	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

	
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	sex = models.CharField(max_length=1,choices=GENDER_CHOICES)
	email = models.EmailField(max_length = 100)
	cellphone = models.IntegerField(default=0)
	phone = models.IntegerField(default=0)
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	profession = models.CharField(max_length = 100)

	def __str__(self):
		comp = self.first_name + ' ' +self.last_name
		return comp