from django.contrib import admin
from .models import mainNew, professionNew, tablePrice

@admin.register(mainNew)
class mainNewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image')

@admin.register(professionNew)
class professionNewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'image')

@admin.register(tablePrice)
class tablePriceAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'price')

