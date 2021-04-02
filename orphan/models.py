from django.db import models

# Create your models here.
class Orphan(models.Model):
    title = models.CharField(max_length=125)
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title