from django.contrib import admin

# Register your models here.
from accounts.models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email','is_staff','is_governmentEmployee','is_trainer',
                    'is_student')


admin.site.register(User,UserAdmin)
