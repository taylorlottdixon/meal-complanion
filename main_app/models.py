from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    prep_time = models.IntegerField(help_text='minutes')
    cook_time = models.IntegerField(help_text='minutes')
    servings = models.IntegerField()
    serving_size = models.CharField(max_length=10)
    instructions = RichTextField()
    ingredients = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)