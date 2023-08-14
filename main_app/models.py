from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User


COLORS = (
    ('Wi', 'White'),
    ('LP', 'Light Purple'),
    ('LB', 'Light Blue'),
    ('Rd', "Red"),
    ('Yw', 'Yellow'),
    ('Gn', 'Green'),
    ('Or', 'Orange'),
    ('Pk', 'Pink'),
    ('Ba', 'Black'),
    ('Tl', 'Teal'),
    ('LG', 'Light Grey'),
    ('DG', 'Dark Grey'),
    ('DB', 'Dark Blue'),
    ('Mr', 'Maroon'),
    ('Gl', 'Gold'),
    ('DP', 'Dark Purple'),
)

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack'),
)

SIZES = (
    ('TB', 'Tbsp'),
    ('TS', 'Tsp'),
    ('CP', 'Cup'),
    ('QT', 'Quart'),
    ('PT', 'Pint'),
    ('PC', 'Pinch'),
    ('WH', 'Whole'),
    ('SM', 'Small'),
    ('MD', 'Medium'),
    ('LG', 'Large'),
    ('UN', 'Unit'),
)


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField
    serving = models.IntegerField('Amount')
    serving_size = models.CharField(
        max_length=2,
        choices=SIZES,
        default=SIZES[0][0]
    )


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Category {self.name}'


class Tag(models.Model):
    name = models.CharField('Tag Name', max_length=100)
    color = models.CharField(
        'Color',
        max_length=2,
        choices=COLORS,
        default=COLORS[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} Tag'


class Recipe(models.Model):
    name = models.CharField('Recipe Name', max_length=100)
    description = models.TextField('Description', max_length=500)
    prep_time = models.IntegerField('Prep Time', help_text='mins')
    cook_time = models.IntegerField('Cook Time', help_text='mins')
    servings = models.IntegerField('Number of Servings')
    serving_size = models.CharField('Serving Size', max_length=10)
    instructions = RichTextField('Instructions')
    ingredients = models.ManyToManyField(Ingredient, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='recipes', blank=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("recipes_detail", kwargs={'pk': self.id, "recipe_id": self.id})

    def get_total_time(self):
        return self.prep_time + self.cook_time


class Meal(models.Model):
    date = models.DateField('Meal Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    name = f'{date} {meal}'
    recipes = models.ManyToManyField(Recipe, related_name='meals', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("meal_detail", kwargs={'pk': self.id, "meal_id": self.id})
    

class Photo(models.Model):
  url = models.CharField(max_length=200)
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for recipe_id: {self.recipe_id} @{self.url}"