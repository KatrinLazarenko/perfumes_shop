from django.db import models


gender_choice = (
    ("male", "male"),
    ("female", "female"),
    ("unisex", "unisex")
)

type_choice = (
    ("EDP", "EDP"),
    ("EDT", "EDT"),
    ("Cologne", "Cologne"),
    ("Perfumes", "Perfumes")
)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    size = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choice)
    type = models.CharField(max_length=20, choices=type_choice)
    image = models.ImageField(upload_to="catalogue/images/")
