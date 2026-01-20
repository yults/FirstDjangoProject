from django.db import models

class Note(models.Model):
    fio = models.CharField(max_length=256, blank=False, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email', blank=False)
    text = models.TextField(verbose_name='Текст отзыва', blank=False)
    status = models.BooleanField(default=False, verbose_name='Проверено')

    def __str__(self):
        return f'{self.fio} | {self.email} | {self.text}'