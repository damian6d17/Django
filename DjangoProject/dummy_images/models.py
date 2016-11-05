from __future__ import unicode_literals

from django.db import models

class DummyImage(models.Model):
	name = models.CharField(max_length = 20, verbose_name = "Tytul")
	image = models.FileField(upload_to="images/", verbose_name = "Obrazek", null = True)

	def __str__(self):
		return self.name