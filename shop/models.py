from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300,unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('shop:product-list-by-category',args=[self.slug])
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    slug = models.SlugField(max_length=300)
    image = models.ImageField(upload_to=r'products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ['name']
        indexes = [models.Index(fields=['id','slug']),
                   models.Index(fields=['name']),
                   models.Index(fields=['-created'])]
        
    def get_absolute_url(self):
        return reverse('shop:product-detail',args=[self.id,self.slug])
    
    def __str__(self):
        return self.name

    
    


