from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')  # Columns to display in the list view
    list_filter = ('available',)  # Add filters for the availability
    search_fields = ('name',)  # Add a search box for name
    list_editable = ('price', 'available')  # Allow inline editing of price and availability
    ordering = ('name',)  # Default ordering by name


admin.site.register(MenuItem, MenuItemAdmin)
