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
    path('meals/', views.meals_index, name='meals_index'),
    path('meals/<int:pk>/', views.meals_details, name='meals_details'),
    path('meals/create/', views.NewMeal.as_view(), name='meals_create'),
    path('meals/<int:pk>/update/', views.UpdateMeal.as_view(), name='meals_update'),
    path('meals/<int:pk>/delete/', views.DeleteMeal.as_view(), name='meals_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
]

