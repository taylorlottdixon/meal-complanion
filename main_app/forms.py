from django.forms import ModelForm, DateInput
# from django.admin.forms import ModelMultipleChoiceField
from .models import Meal

# class TagForm(ModelForm):
#   class Meta:
#     model = Tag
#     fields = '__all__'

class MealForm(ModelForm):
  class Meta:
    model = Meal
    fields = '__all__'
    widgets = { "date": DateInput(format=('%m/%d/%Y'), attrs={"type": "date"})}

# class RecipeForm(ModelForm):
#   class Meta:
#     model = Recipe
#     fields = '__all__'
#     widgets = {'ingredients': ModelMultipleChoiceField
#       (Ingredient.objects.all(),
#       widget=admin.widgets.RelatedFieldWidgetWrapper(
#             widget=admin.widgets.FilteredSelectMultiple('Ingredient', False),
#             rel=Ingredients.recipes.rel,
#             admin_site=admin.site
#       ),
#       required=False,
#     )
#   }