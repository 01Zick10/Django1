from django.db import models

# Create your models here.


class Pidrov(models.Model):
    name = models.CharField(max_length=16)
    tema = models.CharField(max_length=32)
    info = models.TextField()
    created_at = models.DateField()
    # updated_at = models.DateField(auto_now=True)
    # asdas = models.JSONField()
    # asdsad = models.ImageField()
    # asdasdasd = models.FileField()

    def __str__(self):
        return self.tema

    class Meta:
        verbose_name = 'Новость про Пидора'
        verbose_name_plural = 'Новости про Пидораcов'
        # ordering = ['-created_at']

