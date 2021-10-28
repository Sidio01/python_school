from django.shortcuts import render
from django.http import HttpResponse
from recipebook.models import Recipes, Ingredients, RecipesIngredients


def home(request):
    return HttpResponse("Hello, You're at the home page.")

def recipes(request):
    recipes = Recipes.objects.all()
    # return HttpResponse("Hello, You're at the recipes page.")
    # return HttpResponse(recipe)
    return render(request, 'recipes.html', {'action': 'Display all recipes', 'all_recipes': recipes})