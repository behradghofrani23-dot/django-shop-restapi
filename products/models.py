from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    count=models.IntegerField(default=0)
    Category=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.title