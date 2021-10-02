from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Send email
        send_mail(
            subject,
            message,
            'blessing@primetimecode.co.za',
            [email],

            fail_silently=False,
        )
