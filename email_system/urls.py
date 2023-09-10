# urls.py
from django.urls import path
from .views import EmployeeListView,EventListView, EmailTemplateListView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('email-templates/', EmailTemplateListView.as_view(), name='emailtemplate-list'),
]
