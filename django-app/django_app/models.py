from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Video(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')