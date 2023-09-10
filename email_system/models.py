from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=[
        ('Birthday', 'Birthday'),
        ('Work Anniversary', 'Work Anniversary'),
    ])
    event_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.event_type} on {self.event_date}"

class EmailTemplate(models.Model):
    event_type = models.ForeignKey(Event, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"{self.event_type} Template"
