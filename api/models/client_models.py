from django.db import models


class Client(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    short_description = models.TextField("Краткая характеристика")
    email = models.EmailField()
    phone_number = models.CharField("Телефон", max_length=100)
    store = models.CharField("Магазин", max_length=100)
    birth_day = models.DateField("Дата рождения")


    def __str__(self):
        return self.first_name + ' ' + self.surname
