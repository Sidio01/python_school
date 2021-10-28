from django.db import models

# TODO many to many поля

class Ingredients(models.Model):
    # Модель - ингредиент
    # 1. id
    # 2. наименование (name)
    # 3. единица измерения (measure)
    name = models.CharField("Наименование", max_length=100, null=False)
    measure = models.CharField("Единица измерения", max_length=10, null=False)


class Recipes(models.Model):
    # Модель - рецепты
    # 1. id
    # 2. наименование (name)
    # 3. описание (description)
    # 4. текст рецепта (recipe_text)
    name = models.CharField("Наименование", max_length=200, null=False)
    description = models.TextField("Описание", null=False)
    recipe_text = models.TextField("Текст рецепта", null=False)


class RecipesIngredients(models.Model):
    # Модель рецепт - ингредиент
    # 1. id
    # 2. id рецепта (recipe_id)
    # 3. id ингредиента (ingredient_id)
    # 4. количество (amount)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)