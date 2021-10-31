from django.contrib import admin
import recipebook.models


@admin.register(recipebook.models.Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "description",
        "recipe_text",
    )

    search_fields = (
        "id",
        "name",
        "description",
        "recipe_text",
    )

    ordering = ("id", )


@admin.register(recipebook.models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "measure",
    )

    search_fields = (
        "id",
        "name",
        "measure",
    )

    ordering = ("id", )


@admin.register(recipebook.models.RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "recipe_id",
        "ingredient_id",
        "amount",
    )

    search_fields = (
        "id",
        "recipe_id",
        "ingredient_id",
        "amount",
    )

    ordering = ("id", )
