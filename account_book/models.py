from django.db import models
from user.models import UserModel
# Create your models here.
class account_book(models.Model):
    price=models.IntegerField(blank=None)
    memo=models.CharField(blank=None,max_length=9999)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.memo,self.user