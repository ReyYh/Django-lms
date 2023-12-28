from django.contrib import admin
from .models import Role, RolePermits, Permit, Account


admin.site.register(Role)
admin.site.register(RolePermits)
admin.site.register(Permit)
admin.site.register(Account)
