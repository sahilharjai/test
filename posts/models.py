from django.db import models
from django.contrib.auth.models import User
from activities.models import Notification
# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=100)
	date =models.DateTimeField(auto_now_add=True)

	def notify_commented(self, post):
		Notification(notification_type=Notification.COMMENTED,from_user=self.user, to_user=post.user,post=post).save()