from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(user,receiver):
    subject = 'Welcome to InstaGlam';
    sender = 'daisymoringa100@gmail.com';

    text_content = render_to_string('email/instaemail.txt',{"user": user})
    html_content = render_to_string('email/instaemail.html',{"user": user})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()