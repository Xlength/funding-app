from django.db import models
from django.contrib.auth.models import User

class FundingApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.TextField()
    supporting_documents = models.FileField(upload_to="documents/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.status}"

class ApplicationReview(models.Model):
    application = models.OneToOneField(FundingApplication, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    comments = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Review for {self.application.user.username} - {self.application.status}"
