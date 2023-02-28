from django.db import models
from cloudinary.models import CloudinaryField

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, username, role='Member', is_staff=False, is_superuser=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            username=username,
            role=role,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, name, username, role='Admin', is_staff=True, is_superuser=True, password=None):
        user = self.create_user(
            email=email,
            name=name,
            username=username,
            role=role,
            is_staff=is_staff,
            is_superuser=is_superuser,
            password=password,
        )

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'Admin'
        MEMBER = 'Member'
        GUEST = 'Guest'

    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True
    )
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=25, unique=True, db_index=True)
    profile_photo = CloudinaryField('image', null=True, blank=True)
    background_photo = CloudinaryField('image', null=True, blank=True)
    bio = models.TextField(default='Your bio here', blank=True, null=False)
    role = models.CharField(max_length=15, choices=Role.choices, default='Member', db_index=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'role',]


class UserCloseFriendRelation(models.Model):
    friender = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='friender')
    friended = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='friended')