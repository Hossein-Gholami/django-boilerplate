from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=120)
    price = models.IntegerField(default=10, null=False)
    image = models.CharField(max_length=500, default="https://cdn3.iconfinder.com/data/icons/retail-13/100/location-pin-512.png")

    def __str__(self):
        return self.title
