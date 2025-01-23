from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=100)
    brand = models.CharField("Бренд", max_length=100)
    description = models.TextField("Краткое описание", null=True)
    size = models.FloatField("Объем", null=True)
    fatness = models.FloatField("Жирность", null=True)
    price = models.FloatField("Цена продажи")
    image_url = models.TextField("Изображение")
    good_url = models.TextField("Ссылка на товар")


    def __str__(self):
        return self.name + ' ' + self.brand