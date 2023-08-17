from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack'),
)


class Recipe(models.Model):
    name = models.CharField('Recipe Name', max_length=100)
    description = models.TextField('Description', max_length=500)
    prep_time = models.IntegerField('Prep Time (mins)')
    cook_time = models.IntegerField('Cook Time (mins)')
    servings = models.IntegerField('Number of Servings')
    serving_size = models.CharField('Serving Size', max_length=10)
    instructions = models.TextField('Instructions')
    ingredients = models.TextField('Ingredients', max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("recipes_details", kwargs={"recipe_id": self.id})

    def get_total_time(self):
        return self.prep_time + self.cook_time


class Meal(models.Model):
    name = models.CharField('Meal Name', max_length=50)
    date = models.DateField('Meal Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    recipes = models.ManyToManyField(
        Recipe, 
        related_name='meals', 
        blank=True, 
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.meal}'
    
    def get_absolute_url(self):
        return reverse("meals_details", kwargs={'pk': self.id})
    
    class Meta:
        ordering = ['-date']