# import os
# import uuid
# import boto3
from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Meal, Tag, Category
from .forms import TagForm



# Route for 'Home'
def home(request):
    return render(request, 'home.html')

# Route for 'About'
def about(request):
    return render(request, 'about.html')

# Route for 'Recipes'
@login_required
def recipes_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

# Route for 'Recipe Details'
@login_required
def recipes_details(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    tag_ids = recipe.tags.all().values_list('id')
    tags_available = Tag.objects.exclude(id__in=tag_ids)
    return render(request, 'recipes/detail.html', {
        'recipe': recipe,
        'tags': tags_available,
    })

# Route for 'Create Recipe'
class NewRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'

# Route for 'Updating Recipe'
class UpdateRecipe(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = '__all__'

# Route for 'Deleting Recipe'
class DeleteRecipe(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes'

# Route for 'Adding Photo'

# Route for 'Tags'
@login_required
def tags_index(request):
    tags = Tag.object.filter(user=request.user)
    return render(request, 'tags/index.html', {'tags': tags})

# Route for 'Tags Details'
class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag

# Route for 'Create Tag'
class NewTag(LoginRequiredMixin, CreateView):
    model = Tag
    fields = '__all__'
    success_url = '/recipes'

# Route for 'Updating Tag'
class UpdateTag(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = '__all__'

# Route for 'Deleting Tag'
class DeleteTag(LoginRequiredMixin, DeleteView):
    model = Tag

# Add new tag from recipe detail
@login_required
def add_tag(request, recipe_id):
  form = TagForm(request.POST)
  if form.is_valid():
    new_tag = form.save(commit=False)
    new_tag.save()
  return redirect('detail', recipe_id=recipe_id)

# Associate a tag with a recipe
@login_required
def assoc_tag(request, recipe_id, tag_id):
    Recipe.objects.get(id=recipe_id).tags.add(tag_id)
    return redirect('detail', recipe_id=recipe_id)

# Unassociate a tag from a recipe
@login_required
def unassoc_tag(request, recipe_id, tag_id):
    Recipe.objects.get(id=recipe_id).tags.remove(tag_id)
    return redirect('detail', recipe_id=recipe_id)

# Route for 'Meals'
@login_required
def meals_index(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'meals/index.html', {'meals': meals})

# Route for 'Meal Details'
@login_required
def meals_details(request, meal_id):
    meal = Meal.object.get(id=meal_id)
    return render(request, 'meals/detail.html', {
        'meal': meal,
    })

# Route for 'Create Recipe'
class NewMeal(LoginRequiredMixin, CreateView):
    model = Meal
    fields = '__all__'

# Route for 'Updating Recipe'
class UpdateMeal(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = '__all__'

# Route for 'Deleting Recipe'
class DeleteMeal(LoginRequiredMixin, DeleteView):
    model = Meal

# Route for user sign up
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)