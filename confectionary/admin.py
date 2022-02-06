from django.contrib import admin
from .models import Confectionary, Category


class ConfectionaryAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'favourite',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Confectionary, ConfectionaryAdmin)
admin.site.register(Category, CategoryAdmin)
