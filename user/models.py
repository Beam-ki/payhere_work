from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
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

    def create_superuser(self, email, profilename, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        instance = self.create_user(
            email = email,
            password=password,
        )
        instance.is_admin = True
        instance.save(using=self._db)
        return instance

    

class  UserModel(AbstractBaseUser):
    email=models.EmailField('이메일',unique=True)
    password=models.CharField('패스워드',max_length=30)

    objects = MyUserManager()
    
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