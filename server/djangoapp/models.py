from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# CarMake Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # String representation of CarMake
    def __str__(self):
        return self.name  # Return the name as the string representation


# CarModel Model
class CarModel(models.Model):
    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    # Car type choices
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("UTE", "Ute"),
        ("WAGON", "Wagon"),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2000)],
    )

    # String representation of CarModel
    def __str__(self):
        return self.name  # Return the name as the string representation
