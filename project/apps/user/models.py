import uuid

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.db import models
# from project.core.storage_backends import PrivateMediaStorage
from project.apps.common import models as common_models
# from project.apps.facilities import models as facility_models
# from project.apps.super_admin import models as role_models
from project.core.models import BaseModel
from project.core.storage import profile_photo_path


class UserManager(BaseUserManager):

    def create_user(self, email=None, password=None, country_code=None, mobile=None):
        if email:
            user = self.model(email=email.lower(), )
            user.set_password(password)
            user.save(using=self._db)
            user.is_staff = True
            return user
        else:
            user = self.model(mobile=mobile, country_code=country_code)
            user.save(using=self._db)
            user.is_staff = True
            return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password)
        user.user_type = Profile.FINUMO_ADMIN
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    FINUMO_ADMIN = 'FA'
    VENDOR_USER = 'VS'
    CUSTOMER_USER = 'CU'

    USER_TYPE_CHOICE = (
        (FINUMO_ADMIN, 'Finumo Admin'),
        (VENDOR_USER, 'Vendor User'),
        (CUSTOMER_USER, 'Customer User'),
    )

    ACTIVE = 'ACTIVE'
    BLOCKED = 'BLOCKED'
    STATUS_CHOICE = (
        (ACTIVE, 'Active'),
        (BLOCKED, 'Blocked'),
    )

    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=5, blank=True, null=True, choices=USER_TYPE_CHOICE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    profile_photo = models.FileField(upload_to=profile_photo_path, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    email_verified = models.BooleanField(default=False, editable=False)
    country_code = models.CharField(max_length=6, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True, db_index=True)
    mobile_verified = models.BooleanField(default=False, editable=False)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICE)
    dob = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default=ACTIVE)
    is_active = models.BooleanField(default=True)
    # facility = models.ForeignKey(facility_models.Profile, on_delete=models.RESTRICT, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(default=None, null=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.email = self.email.lower() if self.email else None
        return super(Profile, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'mobile', 'country_code'], name='unique_user_constraint')
        ]
        db_table = "user_profile"

    def __str__(self):
        return '{}:{} {}'.format(self.email, self.user_type, self.id)


class Address(BaseModel):
    user = models.OneToOneField(Profile, related_name='address', on_delete=models.CASCADE, null=True, blank=True)
    address_type = models.CharField(max_length=20, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(common_models.State, on_delete=models.RESTRICT, null=True, blank=True)
    zipcode = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{}: {}, {}'.format(self.id, self.address_line1, self.address_line2)