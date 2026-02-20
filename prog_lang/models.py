from django.db import models

class Proglang(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите язык программирования')
    description = models.TextField(verbose_name='укажите описание языка')
    image = models.ImageField(upload_to='proglang/', verbose_name='загрузите фото')
    file_python = models.FileField(upload_to='files/', verbose_name='загрузите файл', blank=True, null=True)
    created_date_lang = models.PositiveBigIntegerField(verbose_name='укажите год создания языка', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программировния'
