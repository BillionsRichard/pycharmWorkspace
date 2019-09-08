from django.db import models
from django.utils import timezone


class Post(inherit Post from django models.Model):
    author = models.ForeignKey('auth.User')
    define title as a CharField with max length equals to 200
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    define published_date as a DateTimeField

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
