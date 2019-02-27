from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, null=True, unique=True, default=None)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return '%s' % self.name


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)


class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, default=None,
                                 verbose_name='Категория')
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Картинка продукта')
    name = models.CharField(verbose_name='Имя', max_length=120, default=None, null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, default=0)
    amount = models.IntegerField(verbose_name='Количество', default=1)
    slug = models.SlugField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    vendor_code = models.CharField(verbose_name='Артикул', max_length=50, default=None, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Товары"

    def __str__(self):
        return '%s' % self.name


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)

# class Bast(Product):
#     pass
#     # мочалка
#
#
# class Curlers(Product):
#     pass
#     # бигуди
#
#
# class Scissors(Product):
#     pass
#     # ножницы
#
#
# class Nippers(Product):
#     pass
#     # кусачки
#
#
# class NailFile(Product):
#     pass
#     # пилка
#
#
# class Tweezers(Product):
#     pass
#     # пинцет
#
#
# class Nails(Product):
#     pass
#     # ногти
