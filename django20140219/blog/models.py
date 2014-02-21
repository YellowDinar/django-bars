from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    date = models.DateTimeField()
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    date = models.DateTimeField()
    def __unicode__(self):
        return self.text