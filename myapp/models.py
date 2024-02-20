from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Recipe {self.id}"
