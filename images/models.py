from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image =models.ImageField(upload_to='images')

    def __str__(self):
        return self.user.username


class ImageResult(models.Model):
    image = models.ForeignKey(UserImage, on_delete=models.CASCADE)
    result = models.CharField(max_length=1000000000)

    def __str__(self):
        return self.result