from django.db import models


class Test(models.Model):
    question = models.CharField(max_length=500, verbose_name='Вопрос')
    explanation = models.CharField(max_length=500, verbose_name='Пояснение')
    photo = models.ImageField(upload_to='test/photo/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Answer(models.Model):
    answer = models.CharField(max_length=500, verbose_name='Ответ')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ')
    test = models.ForeignKey(Test,
                             on_delete=models.CASCADE,
                             verbose_name='Тест',
                             related_name='test')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
