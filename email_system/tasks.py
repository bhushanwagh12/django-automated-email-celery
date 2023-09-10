# email_system/tasks.py
from celery import shared_task
from .utils import send_special_occasion_emails

@shared_task
def send_special_occasion_emails_daily():
    send_special_occasion_emails()
