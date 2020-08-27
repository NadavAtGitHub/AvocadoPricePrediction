from django.db import models


# Create your models here.


class AvocadoOrder(models.Model):
    total_volume = models.DecimalField(max_digits=20, decimal_places=5)
    # TODO: 4046, 4225, 4770 fields are Product LookUp numbers
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

    # TODO: draw from something
    REGIONS = [
        ("Albany", "Albany"),
    ]

    region = models.CharField(choices=REGIONS, max_length=50)
    year = models.IntegerField()

#    ,Date,AveragePrice,Total Volume,4046,4225,4770,Total Bags,Small Bags,Large Bags,XLarge Bags,type,year,region
#   0,2015-12-27,1.33,64236.62,1036.74,54454.85,48.16,8696.87,8603.62,93.25,0.0,conventional,2015,Albany

# ('index', '0')
# ('Date', '2015-12-27')
# ('AveragePrice', '1.33')
# ('Total Volume', '64236.62')
# ('4046', '1036.74')
# ('4225', '54454.85')
# ('4770', '48.16')
# ('Total Bags', '8696.87')
# ('Small Bags', '8603.62')
# ('Large Bags', '93.25')
# ('XLarge Bags', '0.0')
# ('type', 'conventional')
# ('year', '2015')
# ('region', 'Albany')
