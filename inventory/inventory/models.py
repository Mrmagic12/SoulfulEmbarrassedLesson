from django.db import models

class AbstractBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    class Meta:
        abstract = True

class User(AbstractBase):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20)

class Supplier(AbstractBase):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    address = models.TextField()

class Brand(AbstractBase):
    name = models.CharField(max_length=255)

    @property
    def item_name(self):
        try:
            return self.product_set.first().name
        except:
            return None

class Product(AbstractBase):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class Item(AbstractBase):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class PurchaseOrder(AbstractBase):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class PurchaseOrderItem(AbstractBase):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CustomerOrder(AbstractBase):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class CustomerOrderItem(AbstractBase):
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(AbstractBase):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20)

    @property
    def id(self):
        return self.pk