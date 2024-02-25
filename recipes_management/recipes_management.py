import pandas as pd
from myapp.models import Recipe


def recipe_searcher(ing):
    matched_recipes = []
    ing_list = ing.lower().split()  # List of ingredients from input, lowercase
    for recipe in Recipe.objects.all():
        recipe_ingredients = []
        for ing in recipe.ingredient.all():
            recipe_ingredients.append(str(ing.name))
        common_ingredients = [ing for ing in recipe_ingredients if ing in ing_list]
        if len(common_ingredients) == len(recipe_ingredients):
            matched_recipes.append(recipe.description)

    if len(matched_recipes) == 0:
        return ['Unfortunately, we have not matched any of the recipes to the given ingredients']

    return matched_recipes

