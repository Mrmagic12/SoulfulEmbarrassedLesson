from django.db import models

class AbstractBase(models.Model):
  id = models.BigAutoField(primary_key=True)

  class Meta:
    abstract = True

class Item(AbstractBase):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.PositiveIntegerField()

class Brand(AbstractBase):
  name = models.CharField(max_length=100),
  description = models.TextField(blank=True),
  image = models.ImageField(upload_to='brand_images', blank=True)
  item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='brand')
  
  @property
  def item_name(self):
    try:
      return self.item.name
    except:
      return None

class Product(AbstractBase):
  name = models.CharField(max_length=100),
  description = models.TextField(blank=True),
  image = models.ImageField(upload_to='product_images', blank=True)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product')
  
  @property
  def brand_name(self):
    try:
      return self.brand.name
    except:
      return None

class Supplier(AbstractBase):
  name = models.CharField(max_legth=100),
  phone = models.CharField(max_length=255),
  email = models.EmailField(max_length=255),
  address = models.TextField(blank=True)

  item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='supplier')

  @property
  def item_name(self):
    try:
      return self.item.name
    except:
      return None

