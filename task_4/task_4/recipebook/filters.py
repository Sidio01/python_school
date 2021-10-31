from django.db.models import fields
import django_filters

import recipebook.models

class RecipeFilter(django_filters.FilterSet):
    """Фильтр рецептов."""
    class Meta:
        model = recipebook.models.RecipeIngredient
        fields = ['recipe_id', 'ingredient_id']