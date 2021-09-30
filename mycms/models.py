from django.db import models


class CMS(models.Model):
    company_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='cms/%Y/%m/%d/')
    about_me = models.TextField(blank=True)
    linkedin = models.URLField(max_length=200)
    youtube = models.URLField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'CMS'
        verbose_name_plural = 'CMS'

    def __str__(self):
        return self.company_name
