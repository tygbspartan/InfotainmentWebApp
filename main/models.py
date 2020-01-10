from django.db import models


# Create your models here.
#GENRE, USER, MOVIES&TV, REVIEWS
class User(models.Model):
	user_id = models.AutoField(primary_key = True)
	user_name = models.CharField(max_length=40)
	user_email = models.EmailField()
	user_password = models.CharField(max_length=20)
	user_description = models.TextField()


class Feedback(models.Model):
	feedback_id = models.AutoField(primary_key=True)
	feedback_date = models.DateTimeField(auto_now_add=True)
	feedback_body = models.TextField()
	users = models.ForeignKey(User, on_delete=models.CASCADE)

	# TODO shows=models



	#watchlist,fav......feedback/property....
	