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
        )
        instance.set_password(password)
        instance.save(using=self._db)
        return instance
    

class  UserModel(AbstractBaseUser):
    email=models.EmailField('이메일',unique=True,error_messages={"이미 사용중인 이메일입니다"})
    password=models.CharField('패스워드',max_length=30)

    objects = CreateUser()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the instance have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the instance have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True