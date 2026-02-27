from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    age=models.IntegerField(default=0)
    address = models.TextField()
    

    def __str__(self):
        return self.user.username

#on_delete=models.CASCADE means when the parent object is deleted, all related child objects are also deleted automatically.

class Policy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="policies")
    policy_number = models.CharField(max_length=20, unique=True)
    policy_type = models.CharField(max_length=50)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.policy_number


class PremiumPayment(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.policy.policy_number} - {self.amount}"


class Claim(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name="claims")
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    claim_status = models.CharField(max_length=20, default="Pending")
    claim_date = models.DateField()

    def __str__(self):
        return f"{self.policy.policy_number} - {self.claim_status}"
    
class Fundtranfer(models.Model):
    old_policy=models.PositiveIntegerField(unique=True)
    new_policy_no=models.PositiveIntegerField(unique=True)
    customer_name=models.CharField(max_length=100)
    transfer_amount=models.DecimalField(max_digits=10,decimal_places=2)
    transfer_reason=models.TextField()
    status=models.CharField(max_length=50,choices=[
        ('pending','pending'),
        ('approved','approved'),
        ('rejected','rejected')
    ],default='pending')
    is_active=models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.customer_name
    
