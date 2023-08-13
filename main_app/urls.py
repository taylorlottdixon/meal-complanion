from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.recipes_index, name='recipes_index'),
  path('recipes/<int:recipe_id>/', views.recipes_details, name='recipes_detail'),
  path('recipes/create/', views.NewRecipe.as_view(), name='recipes_create'),
  path('recipes/<int:recipe_id>/update/', views.UpdateRecipe.as_view(), name='recipes_update'),
  path('recipes/<int:recipe_id>/delete/', views.DeleteRecipe.as_view(), name='recipes_delete'),
  path('meals/', views.meals_index, name='meals_index'),
  path('meals/<int:meal_id>/', views.meals_details, name='detail'),
  path('meals/create/', views.NewMeal.as_view(), name='meals_create'),
  path('meals/<int:meal_id>/update/', views.UpdateMeal.as_view(), name='meals_update'),
  path('meals/<int:meal_id>/delete/', views.DeleteMeal.as_view(), name='meals_delete'),
#   path('recipes/<int:recipe_id>/add_photo/', views.add_photo, name='add_photo'),
  path('recipes/<int:recipe_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
  path('recipes/<int:recipe_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc_tag'),
  path('tags/', views.tags_index, name='tags_index'),
  path('tags/<int:tag_id>/', views.TagDetail.as_view(), name='tags_detail'),
  path('tags/create/', views.NewTag.as_view(), name='tags_create'),
  path('tags/<int:tag_id>/update/', views.UpdateTag.as_view(), name='tags_update'),
  path('tags/<int:tag_id>/delete/', views.DeleteTag.as_view(), name='tags_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]