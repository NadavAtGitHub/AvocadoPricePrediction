from django.db import models


# Create your models here.


class AvocadoOrder(models.Model):
    total_volume = models.DecimalField(max_digits=20, decimal_places=5)

    # 4046, 4225, 4770 fields are Product LookUp numbers
    num_plu_4046 = models.DecimalField(max_digits=20, decimal_places=5)
    num_plu_4225 = models.DecimalField(max_digits=20, decimal_places=5)

    total_bags = models.DecimalField(max_digits=20, decimal_places=5)
    num_plu_4770 = models.DecimalField(max_digits=20, decimal_places=5)
    small_bags = models.DecimalField(max_digits=20, decimal_places=5)
    large_bags = models.DecimalField(max_digits=20, decimal_places=5)
    extra_large_bags = models.DecimalField(max_digits=20, decimal_places=5)

    AVOCADO_TYPES = [
        ("conventional", "conventional"),
        ("organic", "organic")
    ]
    type = models.CharField(choices=AVOCADO_TYPES, max_length=50)

    REGIONS = [
        ("Albany", "Albany"),
    ]

    region = models.CharField(choices=REGIONS, max_length=50)
    year = models.IntegerField()
