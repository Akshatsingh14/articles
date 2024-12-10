from django.contrib import admin
from .models import Games

# Register your models here.
@admin.register(Games)
class AdminStudent(admin.ModelAdmin):
    list_display = ['name','company','price','genre','quantity','rating','desc']
    list_display_links = ['company']