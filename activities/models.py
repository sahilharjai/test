from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Activity(models.Model):
    COMMENT = 'C'
    ACTIVITY_TYPES = (
        (COMMENT, 'comment'),
        
        )

    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    post = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.activity_type


class Notification(models.Model):

    COMMENTED = 'C'
    NOTIFICATION_TYPES = (
        (COMMENTED, 'Commented'),
        )

    from_user = models.ForeignKey(User,related_name="sender")
    to_user = models.ForeignKey(User,related_name="receiver")
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('posts.Post', null=True, blank=True)
    notification_type = models.CharField(max_length=1,
                                         choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    class Meta:
        ordering = ('-date',)
