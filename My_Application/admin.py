from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fieldsets = (_('Member Details'),
                 {'fields': (('first_name', 'last_name'), ('dob', 'age'), 'membership_type')}),

    list_display = ['first_name', 'last_name', 'dob', 'age', 'membership_type']
