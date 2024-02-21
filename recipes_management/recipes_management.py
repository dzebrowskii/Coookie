import pandas as pd
from myapp.models import Recipe


def recipe_searcher(ing):
    x = []
    ing = ing.lower().split()

    for recipe in Recipe.objects.all():
        ingredients_list = recipe.ingredients.lower().split()
        if any(ingredient in ingredients_list for ingredient in ing) and all(ingredient in ing for ingredient in ingredients_list):
            x.append(recipe.description)

    if len(x) == 0:
        return ['Unfortunately, we have not matched any of the recipes to the given ingredients']

    return x