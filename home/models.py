from django.db import models


# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pic = models.ImageField(upload_to="pics")
    # special = models.BooleanField(default = False)
    star = models.FloatField(default=5.0)
    genre = models.CharField(max_length=30, default="Action")
    actors = models.TextField(max_length=500)
    runtime = models.IntegerField(default=60)
    year = models.IntegerField(default=2021)
    is_popular = models.BooleanField(default=False)
    is_top_rated = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    price = models.IntegerField(default=10000)
    day = models.IntegerField(default=2)

    def isTopRate(self):
        return True if self.star >= 8.0 else False

    def Showday(self):
        return self.day if self.day in [2, 4, 6, 7] else None

    def __str__(self):
        return self.name
