from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('recipes/<int:recipe_id>/', views.recipes_details, name='recipes_details'),
    path('recipes/create/', views.NewRecipe.as_view(), name='recipes_create'),
    path('recipes/<int:pk>/update/', views.UpdateRecipe.as_view(), name='recipes_update'),
    path('recipes/<int:pk>/delete/', views.DeleteRecipe.as_view(), name='recipes_delete'),
    path('recipes/<int:recipe_id>/add_tag/', views.add_tag, name='add_tag'),
    path('recipes/<int:recipe_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('meals/', views.meals_index, name='meals_index'),
    path('meals/<int:pk>/', views.meals_details, name='meal_detail'),
    path('meals/create/', views.NewMeal.as_view(), name='meals_create'),
    path('meals/<int:pk>/update/', views.UpdateMeal.as_view(), name='meals_update'),
    path('meals/<int:pk>/delete/', views.DeleteMeal.as_view(), name='meals_delete'),
    path('recipes/<int:recipe_id>/add_photo/', views.add_photo, name='add_photo'),
    path('recipes/<int:recipe_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc_tag'),
    path('tags/', views.tags_index, name='tags_index'),
    path('tags/<int:tag_id>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.NewTag.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.UpdateTag.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.DeleteTag.as_view(), name='tags_delete'),
    path('ingredients/<int:ingredient_id>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.NewIngredient.as_view(), name='ingredients_create'),
    path('ingredients/<int:ingredient_id>/update/', views.UpdateIngredient.as_view(), name='ingredients_update'),
    path('ingredients/<int:ingredient_id>/delete/', views.DeleteIngredient.as_view(), name='ingredients_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
]

