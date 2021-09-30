from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = ' Projects'

    def __str__(self):
        return self.title
