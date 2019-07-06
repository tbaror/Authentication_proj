from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/')
    

    

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
