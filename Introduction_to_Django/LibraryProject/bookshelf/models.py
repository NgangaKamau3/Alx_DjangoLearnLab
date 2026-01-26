from django.db import models

class Book(models.Model):
	"""A class to store information about the books on our bookshelf."""
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	publication_year = models.IntegerField()

