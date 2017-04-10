from django.contrib import admin
from .models import Categories, SimpleOfert
# Register your models here.

@admin.register(SimpleOfert)
class SimpleOfert(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'price', 'image_field', 'created_at', 'category')
    search_fields = ('title', )


@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ('title', )
