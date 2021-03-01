from django.db import models

# Masters
from authentification.models import User


class Provider(models.Model):
    name = models.CharField(max_length=255)
    cif = models.CharField(max_length=11)
    address = models.TextField()

    def __str__(self):
        return self.name


class ItemGroup(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Items(models.Model):
    name = models.CharField(max_length=255)
    stock_amount = models.FloatField(default=0)
    order_amount = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    type = models.ForeignKey(ItemGroup, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ItemProfile(models.Model):
    item = models.OneToOneField(Items, on_delete=models.SET_NULL, null=True)
    per_fat = models.FloatField()
    per_sugar_raw = models.FloatField()
    per_sugar_cooked = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Items)

    def __str__(self):
        return self.name


class Order(models.Model):
    deliver_datetime = models.DateTimeField()
    deliver_address = models.CharField(max_length=255)
    deliver_notes = models.TextField()

    delivered = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SubscriptionType(models.Model):
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Subscription(models.Model):
    type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscriptions')
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.start_date) + ' - ' + str(self.end_date)
