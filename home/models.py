from django.db import models
from main.models import User, Feedback

class Shows(models.Model):
	shows_id = models.AutoField(primary_key = True)
	shows_name = models.CharField(max_length = 50)
	shows_description = models.TextField()
	shows_type = models.CharField(max_length = 20) #choices = (('Movie'), ('Series'))
	users= models.ManyToManyField(User) #on delete error
	feedback= models.ForeignKey(Feedback, on_delete=models.CASCADE)
# Create your models here.

	def __str__(self):
		return self.shows_name


class Genre(models.Model):
	genre_id = models.AutoField(primary_key=True)
	genre_name = models.CharField(max_length=40) 
	shows= models.ForeignKey(Shows, on_delete=models.CASCADE)

	def __str__(self):
		return self.genre_name