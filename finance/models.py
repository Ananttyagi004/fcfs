from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile({self.user.username})"
    
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    def __str__(self):
        return f"{self.name}"
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category =models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Transaction({self.amount}, {self.category}, {self.date})"
    
class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="savings_goals")
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField()
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_progress(self):
        return self.progress

    def __str__(self):
        return f"SavingsGoal({self.target_amount}, {self.target_date}, Progress: {self.progress})"

