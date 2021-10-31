from django.db import models


class Ingredient(models.Model):
    """Ингредиент."""
    name = models.CharField("Наименование", max_length=100, null=False)
    measure = models.CharField("Единица измерения", max_length=10, null=False)

    def __str__(self):
        return f'{self.name}, {self.measure}'


class Recipe(models.Model):
    """Рецепт."""
    name = models.CharField("Наименование", max_length=200, null=False)
    description = models.TextField("Описание", null=False)
    recipe_text = models.TextField("Текст рецепта", null=False)
    image = models.URLField("Фотография", default='https://i.pinimg.com/originals/fb/20/09/fb2009a49ef5bbd05adc173956cf83af.jpg')

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """Ингредиенты, указанные в рецепте."""
    recipe_id = models.ForeignKey(Recipe, verbose_name="Рецепт", on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, verbose_name="Ингредиент", on_delete=models.CASCADE)
    amount = models.IntegerField("Количество", null=False)
