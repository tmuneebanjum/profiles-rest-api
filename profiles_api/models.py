from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    
    """ Database model for users in the system. """
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    
    def get_full_name(self): 
        """Return name of user"""
        
        return self.name
    
    def get_short_name(self):
        """retrive short name"""   
        
        return self.name
    
    def __str__(self):
        """return string represenatation of our user"""
        return self.email