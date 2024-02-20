import pandas as pd


def recipe_searcher(ing):  # recipes management
    x = []
    ing = ing.lower().split()

    df = pd.read_csv('recipes.csv')
    for index, row in df.iterrows():
        ingredients_list = row['ingredients'].lower().split()

        if any(ingredient in ingredients_list for ingredient in ing) and all(
                ingredient in ing for ingredient in ingredients_list):
            x.append(row['description'])

    if len(x) == 0:
        text = ['Unfortunately, we have not matched any of the recipes to the given ingredients']

        return text

    return x