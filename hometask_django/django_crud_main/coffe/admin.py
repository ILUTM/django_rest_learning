from django.contrib import admin
from .models import Coffee


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'drink_type', 'price_small', 'price_medium', 'price_large']
    search_fields = ['id', 'drink_type', 'price_small', 'price_medium', 'price_large']
    list_filter = ['id', 'drink_type']


admin.site.register(Coffee, CoffeeAdmin)

