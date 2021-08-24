from django.db import models

# Create your models here.


class Products(models.Model):
    '''
    this is model class for creating product models
    '''

    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

