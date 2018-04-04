from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField

class Ad(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	author = models.ForeignKey(
		on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Объявление'
		verbose_name_plural = 'Объявления'


class Companys(models.Model):
	first_name = models.CharField(max_length=35)
	last_name = models.CharField(max_length=40)
	middle_name = models.CharField(max_length=40)
	phone_number = PhoneNumberField()
	position = models.CharField(max_length=200, db_index=True)
	company_name = models.CharField(max_length=200, db_index=True,unique=True)
	company_type = models.CharField(max_length=20)
	company_adress = models.CharField(max_length=200, db_index=True)
	email = models.EmailField(blank=True, null=True,unique=True)
	site = models.URLField(blank=True, null=True)
	ads = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return f"{self.last_name} {self.first_name}: {self.company_name}"
	class Meta:
		verbose_name = 'Компания'
		verbose_name_plural = 'Компании'

	
	
		