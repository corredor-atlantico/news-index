from django.contrib import admin

# Register your models here.
# Define a new User admin
from core.models import Provider, Items, Recipe, Order, Subscription, SubscriptionType, ItemGroup, ItemProfile


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemProfile)
class ItemProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    pass
