from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=120)
    price = models.IntegerField(default=10, null=False)

    def __str__(self):
        return self.title
