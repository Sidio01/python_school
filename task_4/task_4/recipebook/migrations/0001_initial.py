# Generated by Django 3.2.8 on 2021-10-28 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('measure', models.CharField(max_length=10, verbose_name='Единица измерения')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('recipe_text', models.TextField(verbose_name='Текст рецепта')),
            ],
        ),
        migrations.CreateModel(
            name='RecipesIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipebook.ingredients')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipebook.recipes')),
            ],
        ),
    ]
