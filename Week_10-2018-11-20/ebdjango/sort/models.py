from django.db import models

# Create your models here.
class Book(models.Model):
	link = models.CharField(max_length=100,null=False)
	title = models.CharField(max_length=255,null=False)
	img_url = models.CharField(max_length=255)
	author = models.CharField(max_length=50)
	rating = models.FloatField(max_length=5,null=False)
	ratingsCount = models.IntegerField(null=False)
	genre_type = models.CharField(max_length=20,null=True)
	publish_year = models.IntegerField(null=False)
    description = models.TextField()