from django.contrib import admin
# Register your models here.
from core.models import Message, New, Tag


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass