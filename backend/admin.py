from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.produkgame)
class produkgame(admin.ModelAdmin):
    list_display = ('id', 'title', 'gambar')

@admin.register(models.nominaltopup)
class nominaltopup(admin.ModelAdmin):
    list_display = ('id', 'title', 'produkgameid')

@admin.register(models.transaksitopup)
class transaksitopup(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'nominaltopupid', 'harga', 'datatransaksi', 'statustransaksiid' )

@admin.register(models.statustransaksi)
class statustransaksi(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')