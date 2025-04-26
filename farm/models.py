from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField(null=True,blank=True)  # Added
    fertilizer_type = models.CharField(max_length=100)

class Livestock(models.Model):
    type = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.type} - {self.count}'

class FinancialRecord(models.Model):
    TRANSACTION_TYPES = [('Income', 'Income'), ('Expense', 'Expense')]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Worker(models.Model):
    name = models.CharField(max_length=100)
    task_assigned = models.CharField(max_length=100)
    hours_worked = models.IntegerField()
    start_date = models.DateField(null=True,blank=True)  # Added
    end_date = models.DateField(null=True,blank=True)    # Added

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    scheduled_date = models.DateField()
    assigned_to = models.CharField(max_length=100)

class Weather(models.Model):
    region = models.CharField(max_length=100)
    forecast_date = models.DateField()
