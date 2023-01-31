from django.db import models
from django.db.models import AutoField
from django_extensions.db.fields import ShortUUIDField
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
)


# Create your models here.
class produkgame(
    TitleDescriptionModel,
    models.Model):

    gambar = models.ImageField(upload_to='img/')

    class Meta:
        verbose_name = 'Produk Game'
        verbose_name_plural = 'Produk Game'

    def __str__(self):
        return self.title

class nominaltopup(
    TitleDescriptionModel,
    ActivatorModel,
    models.Model):

    harga = models.IntegerField()
    produkgameid = models.ForeignKey('produkgame', on_delete=models.PROTECT, null=True, related_name='produkgameid')
    gambar = models.ImageField(upload_to='img/')

    class Meta:
        verbose_name = 'Nominal Top Up'
        verbose_name_plural = 'Nominal Top Up'

    def __str__(self):
        return self.title

class transaksitopup(
    TimeStampedModel,
    models.Model):

    id = models.AutoField(primary_key=True)
    invoice = models.CharField(max_length=100, null=True,)
    nominaltopupid = models.ForeignKey('nominaltopup', on_delete=models.PROTECT, null=False, related_name='nominaltopupid')
    harga = models.IntegerField()
    datatransaksi = models.JSONField()
    statustransaksiid = models.ForeignKey('statustransaksi', on_delete=models.PROTECT, null=False, related_name='statustransaksiid')

    class Meta:
        verbose_name = 'Transaksi Top Up'
        verbose_name_plural = 'Transaksi Top Up'

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.invoice, self.nominaltopupid, self.harga, self.datatransaksi, self.statustransaksiid)

class statustransaksi(TitleDescriptionModel,models.Model):
    class Meta:
        verbose_name = 'Status Transaksi'
        verbose_name_plural = 'Status Transaksi'

    def __str__(self):
        return self.title