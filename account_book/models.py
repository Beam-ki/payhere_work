from django.db import models

# Create your models here.
class account_book(models.Model):
    price=models.IntegerField(blank=None)
    memo=models.CharField(blank=None,max_length=9999)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.memo