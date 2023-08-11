from django.db import models
from django.urls import reverse
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User


COLORS = (
    ('Wi', 'White')
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

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Category {self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(
        max_length=2,
        choices=COLORS,
        default=COLORS[0][0]
    )


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='recipes')

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={'pk': self.id, "recipe_id": self.id})