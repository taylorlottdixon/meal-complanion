from django.forms import ModelForm, DateInput
from .models import Tag, Meal

class TagForm(ModelForm):
  class Meta:
    model = Tag
    fields = '__all__'

class MealForm(ModelForm):
  class Meta:
    model = Meal
    fields = '__all__'
    widgets = { "date": DateInput(format=('%m/%d/%Y'), attrs={"type": "date"})}

