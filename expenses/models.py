from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('health', 'Health'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.amount}"