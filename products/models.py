from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Size(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.ForeignKey(
        'Size', on_delete=models.CASCADE, null=False, blank=False)
    color = models.CharField(max_length=100, null=False, blank=False)
    made_in = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
