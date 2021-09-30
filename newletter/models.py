from django.db import models


class Emails(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Emails'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email
