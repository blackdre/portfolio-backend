from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Emails(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Emails'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email


@receiver(post_save, sender=Emails)
def send_new_email(sender, instance, created, **kwargs):

    # If new subscriber is added
    if created:
        email = instance.email if instance.email else "no email given"

        subject = "Welcome to Prime Time Code"
        message = 'Hi! Welcome  to Prime Time Code. '

        send_mail(
            subject,
            message,
            'blessing@primetimecode.co.za',
            [email],

            fail_silently=False,
        )
