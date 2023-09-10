# email_system/email.py
from django.core.mail import send_mail
from email_system.models import Employee

def send_birthday_email(employee):
    subject = 'Happy Birthday!'
    message = f'Happy Birthday, {employee.name}!'
    from_email = 'waghbhushan805@gmail.com'
    recipient_list = [employee.email]
    
    send_mail(subject, message, from_email, recipient_list)

def send_anniversary_email(employee):
    subject = 'Work Anniversary Celebration!'
    message = f'Congratulations, {employee.name}, on your work anniversary!'
    from_email = 'waghbhushan805@gmail.com'
    recipient_list = [employee.email]
    
    send_mail(subject, message, from_email, recipient_list)
