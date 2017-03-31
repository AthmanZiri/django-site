from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Project(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to='porfolio/', default='Images/None/No-img.jpg')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title