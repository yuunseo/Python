from django.contrib import admin
from .models import House
# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    fields = (
        "name",
        "address",
        ("price_per_night","pet_allowed",),
    )

    list_display = ("name", 
        "price_per_night",
        "address",
        "pet_allowed")

    list_filter =("price_per_night",
        "pet_allowed")

    search_fields = ("address",)

    list_editable = ("pet_allowed",)