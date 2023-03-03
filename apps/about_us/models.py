from django.db import models


class Video(models.Model):
    url_video = models.URLField(max_length=1000, verbose_name='Ссылка на видео')
    title = models.CharField(max_length=200, verbose_name='Название видео')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title


class WhatsApp(models.Model):
    url_owner = models.URLField(max_length=1000, verbose_name='Ссылка WA')

    class Meta:
        verbose_name = 'Ссылка WA'
        verbose_name_plural = 'Ссылка WA'

