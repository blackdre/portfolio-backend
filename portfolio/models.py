from django.db import models


class Tutorials(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')

    class Meta:
        verbose_name = ' Tutorials'
        verbose_name_plural = ' Tutorials'

    def __str__(self):
        return self.title
