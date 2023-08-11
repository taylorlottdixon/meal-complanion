from django.shortcuts import render

# Route for 'Home'
class Home(LoginView):
    template_name = 'home.html'

# Route for 'About'
def about(request):
    return render(request, 'about.html')

# Route for 'Recipes'
def recipes_index(request):
    recipes = recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

# Route for 'Recipe Details'
def recipe_details(request, recipe_id):
    recipe = recipe.object.get(id=recipe_id)

# Route for 'Create Recipe'
class NewRecipe():
    model = Recipe

# Route for 'Updating Recipe'
class UpdateRecipe():
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
    tags = tag.object.filter(user=request.user)
    return render(request, 'tags/index.html', {'tags': tags})

# Route for 'Tags Details'
def tags_details(request, tag_id):
    tag = tag.object.get(id=tag_id)

# Route for 'Meals'
