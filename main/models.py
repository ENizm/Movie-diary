from django.db import models


class Film(models.Model):
    name = models.CharField('Название', max_length=25)
    year = models.IntegerField('Год выпуска')
    description = models.TextField('Описание')
    grade = models.FloatField('Моя оценка')
    favorite = models.BooleanField('Избранное')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
