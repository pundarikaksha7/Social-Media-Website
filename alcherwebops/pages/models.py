from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
	username=models.ForeignKey(User,on_delete=models.CASCADE)
	caption=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	picture=models.ImageField(default='media/default.png',upload_to='profile')
	favourites=models.ManyToManyField(User,related_name="favourite",default=None,blank=True)

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})

	def number_of_likes(self):
		return self.likes.count()




# Create your models here.
