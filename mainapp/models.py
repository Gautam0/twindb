from django.db import models

# Create your models here.
class UserInfo(models.Model):
	email_one = models.CharField(max_length=50)
	email_two = models.CharField(max_length=50)

	def __str__(self):
		return (self.email_one + " and " + self.email_two)

class Invitation(models.Model):
	invited_by = models.CharField(max_length=50)

	def __str__(self):
		return (self.invited_by)

class Contact(models.Model):
	name = models.CharField(max_length=30)
	mail = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	message = models.CharField(max_length=500)

	def __str__(self):
		return(self.name + " and " + self.mail + " and " + self.phone + " and " + self.message)
