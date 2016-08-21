from django.db import models


class Recipie(models.Model):
    name = models.CharField('Название рецепта', max_length=255)
    variations = models.ManyToManyField('Variation')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Название ингредиента', max_length=255)

    def __str__(self):
        return self.name


class Variation(models.Model):
    MEASURE_GRAM = 'g'
    MEASURE_LITER = 'l'
    MEASURE_TASTE = 'taste'
    MEASURE_PIECE = 'piece'
    MEASURE_CHOICES = (
        (MEASURE_GRAM, 'г.'),
        (MEASURE_LITER, 'л.'),
        (MEASURE_TASTE, 'по вкусу'),
        (MEASURE_PIECE, 'шт.'),
    )

    ingredient = models.ForeignKey(Ingredient)
    quantity = models.FloatField('Количество', null=True, blank=True)
    measure = models.CharField(
        'Мера', max_length=10, choices=MEASURE_CHOICES, default=MEASURE_TASTE
    )

    def __str__(self):
        return '%s, %s %s' % (
            self.ingredient, self.quantity or '', self.get_measure_display()
        )