from django.contrib import admin
from django.utils.html import format_html
from .models import Mug, Cart


class MugAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:50px;" width="50" />'.format(object.image))

    thumbnail.short_description = 'Mug Image'

    list_display = ('id', 'thumbnail', 'title', 'description', 'price', 'liked')
    list_display_links = ('id', 'thumbnail', 'title')
    list_editable = ('liked', )
    search_fields = ('id', 'title', 'liked',)


class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "mug", "quantity", "payed")
    list_display_links = ('id', 'mug')
    list_editable = ("payed",)


admin.site.register(Cart, CartAdmin)
admin.site.register(Mug, MugAdmin)
