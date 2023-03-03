from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя и возраст')
    text = models.TextField(verbose_name='Содержание отзыва')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title

