from django.db import models

# TODO many to many поля

class Ingredients(models.Model):
    # Модель - ингредиент
    # 1. id
    # 2. наименование (name)
    # 3. единица измерения (measure)

    pass


class Recipes(models.Model):
    # Модель - рецепты
    # 1. id
    # 2. наименование (name)
    # 3. текст рецепта (recipe_text)

    pass


class RecipesIngredients(models.Model):
    # Модель рецепт - ингредиент
    # 1. id
    # 2. id рецепта (recipe_id)
    # 3. id ингредиента (ingredient_id)
    # 4. количество (amount)

    pass