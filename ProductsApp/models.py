from django.db import models

# Create your models here.
class productmodel(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'product_data'

    def __str__(self):
        return self.name


