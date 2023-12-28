from django.db import models
from django.contrib.auth.models import AbstractUser


class RolePermits(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    permit = models.ForeignKey('Permit', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permit')

    def __str__(self):
        return f"{self.role}: {self.permit}"

class Permit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    #role = models.ManyToManyField('Role', through='RolePermission')

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True, null=True)
    permits = models.ManyToManyField(Permit, through='RolePermits', related_name='role_permits')

    def __str__(self):
        return self.name


class Account(AbstractUser):
    #picture = models.ImageField(upload_to='user_pictures/', blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True, related_name='account_role')
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
