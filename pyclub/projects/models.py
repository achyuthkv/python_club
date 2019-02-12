from django.db import models
from django.utils import timezone

class Category(models.Model):
	category_name = models.CharField(max_length=200, blank=True)
	category_image = models.ImageField(upload_to='card-background', blank=True, null=True)
	idkey = models.CharField(max_length=6, default="")
	description = models.CharField(max_length = 140,blank=True, null=True)
	def __str__(self):
		return self.category_name

	class Meta:
		verbose_name_plural = "Categories"

class Components(models.Model):
	title = models.CharField(max_length = 40)
	summary = models.CharField(max_length = 140)
	description = models.TextField()
	cover = models.ImageField(upload_to='images',
							 blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	link = models.URLField(max_length=300, blank=True)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Component"