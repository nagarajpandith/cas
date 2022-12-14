from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (("D", "Desserts"), ("S", "Starters"), ("M", "Main Course"))
MODE_OF_PAYMENT = (("C", "Cash"), ("O", "Online"))

# Extending Django's User model for Canteen Owner & Kitchen Staffs
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    isOwner = models.BooleanField(default=False)
    isKStaff = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    itemNo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    orderItemNo = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    totalAmount = models.FloatField()

    def __str__(self):
        return f"{self.quantity}"

    def get_total_item_price(self):
        return int(self.quantity) * int(self.item.price)

    def save(self, *args, **kwargs):
        self.totalAmount = self.get_total_item_price()
        super().save(*args, **kwargs)


class Order(models.Model):
    tokenNo = models.IntegerField(primary_key=True)
    totalAmount = models.FloatField()
    isCompleted = models.BooleanField(default=False)
    isPaid = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    completedBy = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, blank=True
    )
    modeOfPayment = models.CharField(choices=MODE_OF_PAYMENT, max_length=2)

    def __str__(self):
        return str(self.tokenNo)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def save(self, *args, **kwargs):
        self.totalAmount = self.get_total()
        super().save(*args, **kwargs)


class Bill(models.Model):
    billNo = models.AutoField(primary_key=True)
    amount = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.billNo)
