from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


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
                              max_digits=3,
                              decimal_places=1)
    duration = models.IntegerField(null=False)

    cover = models.ImageField(upload_to = 'images/')

    categories = models.ManyToManyField(Category)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.cover.path)
        width, height = img.size

        if width < height:
            resized_image = img.resize(
                (width, int(height * (width / width)))
            )
            required_loss = (resized_image.size[1] - width)
            resized_image = resized_image.crop(
                box=(0, required_loss / 2, width, resized_image.size[1] - required_loss / 2)
            )
        else:
            resized_image = img.resize(
                (int(width * (height / height)), height)
            )
            required_loss = resized_image.size[0] - height
            resized_image = resized_image.crop(
                box=(required_loss / 2, 0, resized_image.size[0] - required_loss / 2, height)
            )

        resized_image.save(self.cover.path)
