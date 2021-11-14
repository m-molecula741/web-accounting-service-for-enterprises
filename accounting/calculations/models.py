from django.db import models
from datetime import date


class AccInfo(models.Model):
    """Информация"""
    bis_reg_form = models.CharField("форма бизнеса", max_length=40)
    taxation_system = models.CharField("система налогообложения", max_length=40)
    article = models.PositiveIntegerField("артикул товара", blank=True, null=True)
    date_start = models.DateField("дата начала")
    date_end = models.DateField("дата конца")
    profit = models.FloatField("прибыль")


class Income(models.Model):
    """Доходы"""
    product_name = models.CharField("название продукта", max_length=50)
    article = models.PositiveIntegerField("артикул товара")
    date_sales = models.DateField("дата продажи")
    product_price = models.FloatField("цена за единицу")
    product_count = models.PositiveIntegerField("количество")


class Expenses(models.Model):
    """Расходы"""
    product_name = models.CharField("название продукта", max_length=50)
    article = models.PositiveIntegerField("артикул товара")
    date_sales = models.DateField("дата продажи")
    product_price = models.FloatField("цена за единицу")
    product_count = models.PositiveIntegerField("количество")
