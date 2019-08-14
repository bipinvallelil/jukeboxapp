from django.db import models


# Create your models here.

class Video(models.Model):
    url = models.URLField()  #youtube url
    vote = models.IntegerField(default=0) # total votes for each video
    yt_id = models.CharField(max_length=100, unique=True) #field to store youtube id derived from youtube url

    def __str__(self):
        return self.url
