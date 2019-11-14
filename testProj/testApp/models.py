from django.db import models

# Create your models here.

class Episode(models.Model):
    trackId = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.trackId

class Timeline(models.Model):
    headline = models.TextField()
    text = models.TextField()
    event_date = models.DateField()
    media_url = models.URLField()

    def __str__(self):
        return self.headline + " : " + self.text + " : " + str(self.event_date)

