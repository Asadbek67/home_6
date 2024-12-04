from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, related_name="cars", on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.model_name} ({self.year})"

