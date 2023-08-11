# import uuid
# import boto3
from django.shortcuts import render, redirect
# import os

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Meal, Tag, Category



# Route for 'Home'
def home(request):
    return render(request, 'home.html')

# Route for 'About'
def about(request):
    return render(request, 'about.html')

# Route for 'Recipes'
def recipes_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

# Route for 'Recipe Details'
def recipe_details(request, recipe_id):
    recipe = Recipe.object.get(id=recipe_id)
    tag_ids = Recipe.tags.all().values_list('id')
    tags_available = Tag.objects.exclude(id__in=tag_ids)
    return render(request, 'recipes/detail.html', {
        'recipe': recipe,
        'tags': tags_available,
    })

# Route for 'Create Recipe'
class NewRecipe(CreateView):
    model = Recipe

# Route for 'Updating Recipe'
class UpdateRecipe(UpdateView):
    model = Recipe

# Route for 'Deleting Recipe'
class DeleteRecipe(DeleteView):
    model = Recipe

# Route for 'Sign In'
def login(request):
    error_message = ''
    if request.method == 'POST':
        form = UserLogInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:    
            error_message = 'Please try again'
    form = UserLogInForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

# Route for 'Adding Photo'

# Route for 'Tags'
def tags_index(request):
    tags = Tag.object.filter(user=request.user)
    return render(request, 'tags/index.html', {'tags': tags})

# Route for 'Tags Details'
def tags_details(request, tag_id):
    tag = Tag.object.get(id=tag_id)

# Associate a tag with a recipe
def assoc_tag(request, recipe_id, tag_id):
    Recipe.objects.get(id=recipe_id).tags.add(tag_id)
    return redirect('detail', recipe_id=recipe_id)

# Unassociate a tag from a recipe
def unassoc_tag(request, recipe_id, tag_id):
    Recipe.objects.get(id=recipe_id).tags.remove(tag_id)
    return redirect('detail', recipe_id=recipe_id)

# Route for 'Meals'
def meals_index(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'meals/index.html', {'meals': meals})

# Route for 'Meal Details'
def meals_details(request, meal_id):
    meal = Meal.object.get(id=meal_id)
    return render(request, 'meals/detail.html', {
        'meal': meal,
    })

# Route for 'Create Recipe'
class NewMeal(CreateView):
    model = Meal

# Route for 'Updating Recipe'
class UpdateMeal(UpdateView):
    model = Meal

# Route for 'Deleting Recipe'
class DeleteMeal(DeleteView):
    model = Meal

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)