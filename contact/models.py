from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name


@receiver(post_save, sender=Contact)
def send_new_email(sender, instance, created, **kwargs):

    # If new subscriber is added
    if created:
        email = instance.email if instance.email else "no email given"

        subject = instance.subject if instance.subject else "no subject given"
        message = instance.message if instance.message else "no message given"

        send_mail(
            subject,
            message,
            'blessing@primetimecode.co.za',
            ['blessing@primetimecode.co.za'],

            fail_silently=False,
        )
