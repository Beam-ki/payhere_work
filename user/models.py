from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class CreateUser(BaseUserManager):
    
    def creat_user(self,email,password=None):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        instance = self.model(
            email=email,
            password=password
        )
        instance.set_password(password)
        instance.save(using=self._db)
        return instance
    

class  UserModel(AbstractBaseUser):
    email=models.EmailField('email',unique=True,error_messages={"이미 사용중인 이메일입니다"})
    password=models.CharField('password',max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [password]
def __str__(self):
    return self.email