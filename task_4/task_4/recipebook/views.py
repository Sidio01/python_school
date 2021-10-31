from django.shortcuts import render

from recipebook.models import RecipeIngredient
from recipebook.filters import RecipeFilter


def main_page(request):
    """Список рецептов с фильтрацией по названию и ингредиентам."""

    recipes_objects = RecipeIngredient.objects.select_related(
        'recipe_id', 'ingredient_id')
    recipe_filter = RecipeFilter(request.GET, queryset=recipes_objects)
    recipes_objects = recipe_filter.qs.distinct("recipe_id")

    return render(request,
                  'main.html',
                  {
                      'title': 'Каталог рецептов',
                      "recipes_ingredients": recipes_objects,
                      "recipe_filter": recipe_filter,
                      "form_description": "Здесь вы можете ознакомиться с каталогом рецептов",
                  })


def get_recipe_page(request, recipe_id):
    """Страница рецепта."""
    recipe = RecipeIngredient.objects.select_related(
        'recipe_id', 'ingredient_id').filter(recipe_id=recipe_id)
    title = recipe[0].recipe_id.name
    image = recipe[0].recipe_id.image
    recipe_text = recipe[0].recipe_id.recipe_text.replace('\\n', '\n')

    return render(request, 'recipe.html',
                  {
                      'recipe': recipe,
                      'title': title,
                      'image': image,
                      'recipe_text': recipe_text,
                  })
