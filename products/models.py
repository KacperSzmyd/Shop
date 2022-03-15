from django.db import models

class Producer(models.Model):
    name = models.CharField(max_length=100)
    desription = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.plakat.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



