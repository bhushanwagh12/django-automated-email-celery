# email_system/utils.py
from datetime import date
from django.utils import timezone
from .models import Employee, Event
from .email import send_birthday_email, send_anniversary_email

def send_special_occasion_emails():
    today = timezone.now().date()
    
    # Find employees with birthdays today
    birthday_employees = Employee.objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)
    for employee in birthday_employees:
        send_birthday_email(employee)
    
    # Find employees with work anniversaries today
    anniversary_employees = Event.objects.filter(event_date__month=today.month, event_date__day=today.day, event_type='Work Anniversary')
    for event in anniversary_employees:
        send_anniversary_email(event.employee)
