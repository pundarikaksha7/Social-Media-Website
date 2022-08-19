from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default1.png',upload_to='profile_pics')
	bio=models.TextField()

	def __str__(self):
		return "{} Profile".format(self.user.username)

# Create your models here.
