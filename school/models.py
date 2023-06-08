from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Educations(models.Model):
    name = models.ForeignKey('PhotoEducations', on_delete=models.CASCADE, default=1, verbose_name='Название')
    min_age_kids = models.PositiveIntegerField(default=0)
    max_age_kids = models.IntegerField(
        validators=[
            MaxValueValidator(18),
            MinValueValidator(1)
        ]
    )
    about = models.TextField(blank=True, verbose_name='О программе')
    type_edu = models.ForeignKey('Categories', on_delete=models.CASCADE, null=True, verbose_name='Тип программы')

    def get_absolute_url(self):
        return reverse('programma', kwargs={'name': self.name})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программу'
        verbose_name_plural = 'Программы'
        ordering = ['id']


class Categories(models.Model):
    class TypeName(models.TextChoices):
        UCHEBN = "UCH", _("Учебная")
        DOPOLN = "DOP", _("Дополнительная")
        RAZVLEK = "RAZ", _("Развлекающая")

    type_name = models.CharField(
        max_length=3,
        choices=TypeName.choices,
        default=TypeName.UCHEBN,
        verbose_name='Категории'
    )

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class PhotoEducations(models.Model):
    name_edu = models.CharField(max_length=40, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return self.name_edu

    class Meta:
        verbose_name = 'Фото программы'
        verbose_name_plural = 'Фото программ'
