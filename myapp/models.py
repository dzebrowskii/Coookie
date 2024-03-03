from django.db import models




class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"Ingredient {self.name}"


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredient = models.ManyToManyField(Ingredient,related_name='recipes')
    description = models.TextField()

    def __str__(self):
        return f"Recipe {self.name}"
