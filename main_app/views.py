import os
import uuid
import boto3
from django.shortcuts import render, redirect


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Meal
from .forms import MealForm




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
    return render(request, 'recipes/detail.html', {
        'recipe': recipe,
    })

# Route for 'Create Recipe'
class NewRecipe(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'description', 'prep_time', 'cook_time', 'servings', 'serving_size', 'ingredients', 'instructions']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Route for 'Updating Recipe'
class UpdateRecipe(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description', 'prep_time', 'cook_time', 'servings', 'serving_size', 'ingredients', 'instructions']

# Route for 'Deleting Recipe'
class DeleteRecipe(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes'

# Route for 'Meals'
@login_required
def meals_index(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'meals/index.html', {'meals': meals})

# Route for 'Meal Details'
@login_required
def meals_details(request, pk):
    meal = Meal.objects.get(id=pk)
    return render(request, 'meals/details.html', {
        'meal': meal,
    })

# Route for 'Create Recipe'
class NewMeal(LoginRequiredMixin, CreateView):
    model = Meal
    # fields = ['name', 'date', 'meal', 'recipes']
    form_class = MealForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Route for 'Updating Recipe'
class UpdateMeal(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = '__all__'

# Route for 'Deleting Recipe'
class DeleteMeal(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = '/meals'

# Route for user sign up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes_index')
    else:
        error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def profile(request):
    return render(request, 'registration/profile.html')