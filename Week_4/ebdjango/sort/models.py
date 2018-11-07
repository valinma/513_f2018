from django.db import models

class Book(models.Model):
	bookID = models.CharField(max_length=20)
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=50)
	rating = models.FloatField(max_length=5)
	ratingsCount = models.CharField(max_length=50)
	reviewsCount = models.CharField(max_length=50)

	def __str__(self):
		return self.title