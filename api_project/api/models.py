from django.db import models

class Book(models.Model):
	"""A simple book instance."""
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	
