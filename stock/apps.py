from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'stock'
    verbose_name = "Склад"


class StockOnRuConfig(StockConfig):
    verbose_name = "Склад"
