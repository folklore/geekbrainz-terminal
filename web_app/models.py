from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    title = models.CharField(null=False,
                             blank=False,
                             max_length=128)
    description = models.TextField(null=False,
                                   blank=False)
    formula = models.TextField(null=False,
                               blank=False)
    ibu = models.DecimalField(null=False,
                              max_digits=4,
                              decimal_places=2)
    ebc = models.DecimalField(null=False,
                              max_digits=4,
                              decimal_places=2)
    alc = models.DecimalField(null=False,
                              max_digits=4,
                              decimal_places=2)
    duration = models.IntegerField(null=False)

    cover = models.ImageField(upload_to = 'images/')

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.RESTRICT)
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE)
    volume = models.IntegerField(null=False)
    measure = models.CharField(null=False,
                               blank=False,
                               max_length=32)

    def __str__(self):
        return self.product.title
