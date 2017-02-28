from django.db import models



class User(models.Model):
    username = models.CharField(max_length=200)
    signup_time = models.DateTimeField('SignUp Date')

    def __str__(self):
        return self.username

class Calib(models.Model):
    phonename = models.CharField(max_length=200)
    calib_text = models.CharField(max_length=200)
    calib_size = models.CharField(max_length=200)

    def __str__(self):
        return self.phonename


class CalibVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=200)
    video_size = models.CharField(max_length=200)
    phonename = models.CharField(max_length=200)
    calib = models.ForeignKey(Calib)

    def __str__(self):
        return self.video_name



