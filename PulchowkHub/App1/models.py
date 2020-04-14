from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    portfolio_site = models.CharField(max_length=264,blank=True)
    profile_pic = models.ImageField(upload_to = 'Profile_Pictures', blank = True)

    def __str__(self):
        return self.user.username
