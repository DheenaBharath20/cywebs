from django.db import models

# Create your models here.
class Announcements(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.title

        