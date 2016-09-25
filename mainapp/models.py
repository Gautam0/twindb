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

		