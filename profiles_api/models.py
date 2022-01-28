from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin # maybe this is removed from the module..? Throws an error.
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    create_user() will be sued by django CLI to create users.
    """

    def create_user(self, email, name, password=None):
        """
        Create a new user profile
        """
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db) # standard procedure to save the users

        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a new superuser with given details
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True # This is inherited by PermissionMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Databse model for users in the system
    To add a new column to the database:
        1. use models.ColumnName(max_length=255, unique=True, all_other_databse_realted_fields)

    Use a model manager to let django know how to control user defined classes via the django CLI
    """

    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve fullname of the user
        """
        return self.name

    def get_short_name(self):
        """
        Retrive the short name of the user
        """
        return self.name

    def __str__(self):
        """
        Return the string representation of the user
        """
        return self.email


class ProfileFeedItem(models.Model):
    """
    Profile status update
    """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return the model as a string
        """
        return self.status_text
