from django.db import models
from userapp.models import User

class LoanApplication(models.Model):
    LOAN_TYPES = (
        ('personal', 'Personal Loan'),
        ('home', 'Home Loan'),
        ('car', 'Car Loan'),
        ('education', 'Education Loan'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.IntegerField()  
    applied_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_date = models.DateTimeField(blank=True, null=True)
