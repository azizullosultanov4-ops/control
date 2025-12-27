from django.db import models

# Create your models here.
class Control(models.Model):
    title = models.CharField(max_length = 40, verbose_name= "Название сайта ")
    description  = models.TextField(verbose_name= "Описание ")
    phone = models.CharField(max_length=100, verbose_name="Номер телефона ")
    email = models.EmailField(verbose_name="Электронная почта")
    locate = models.CharField(max_length=100, verbose_name="Адрес сайта ")
    logo = models.ImageField(upload_to='logos/',verbose_name="Логотип сайта ") 

    class Meta:
        verbose_name = "Настройка сайта "
        verbose_name_plural = "Настройкии сайта "