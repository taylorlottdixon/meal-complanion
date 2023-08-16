from django.forms import ModelForm
from .models import Tag

class TagForm(ModelForm):
  class Meta:
    model = Tag
    fields = '__all__'

# class IngredientForm(ModelForm):
#     Ingredients.objects.all(),
#     widget=admin.widgets.RelatedFieldWidgetWrapper(
#            widget=admin.widgets.FilteredSelectMultiple('Ingredients', False),
#            rel=Post.ingredients.rel,
#            admin_site=admin.site
#         ),
#     required=False,
