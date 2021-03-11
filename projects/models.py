from django.db import models

# Create your models here.
class Product(models.Model):
    """Model definition for Product."""
    product_category = (
        ('CAKES','cake'),
        ('PASTRIES','pastry'),
        ('BREADS','bread'),
        ('SWEETS','sweet'),
        ('SNACKS','snack'),
    )

    name = models.CharField(max_length=50, default='product')
    price = models.FloatField(default=500.00)
    quantity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='products',default='products/noimage.jpg')
    category = models.CharField(max_length=10,choices=product_category,default=product_category[0][1])

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
