from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class App(models.Model):
    appName = models.CharField(max_length=60)
    appLinks = models.CharField(max_length=60)
    appCategory = models.CharField(max_length=60)
    appSubCategory = models.CharField(max_length=60)
    appPoints = models.IntegerField(null=True, blank=True)
    appImage = models.ImageField(upload_to='AppPics')
    taskCompleted = models.ManyToManyField(User, null=True, blank=True)


    def __str__(self):
        return self.appName

class Task(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenShort = models.ImageField(upload_to='ScreenShort')



