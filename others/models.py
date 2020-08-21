from django.db import models

# Create your models here.

class Others(models.Model):
    title = models.CharField(max_length=125)
    img1 = models.ImageField()
    img2 = models.ImageField()
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
