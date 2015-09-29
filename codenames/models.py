from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
	country = models.CharField(max_length=3)
	longitude = models.DecimalField(max_digits=10, decimal_places=7,null=True)
	latitude = models.DecimalField(max_digits=10, decimal_places=7,null=True)
	def __str__(self):
		return (str(self.longitude) + ' ' + str(self.latitude))

class Agency(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Operation(models.Model):
	code_word = models.CharField(max_length=200)
	location = models.ForeignKey(Location)
	agency = models.ForeignKey(Agency)
	user = models.ForeignKey(User)
	op_num = models.IntegerField()
	clearance = models.CharField(max_length=30)
	def __str__(self):
		return self.code_word