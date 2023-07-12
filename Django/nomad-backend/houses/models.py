from django.db import models

# Create your models here.
class House(models.Model):

    """Model Definition About Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(verbose_name="Pets Allowed?",default=True,help_text="Does this house allow pets?")

    def __str__(self):
        return self.name
    
