from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserCloseFriendRelation

# Register your models here.
User = get_user_model()

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'username', 'role']
    class Meta:
        model = User

class CloseFriendAdmin(admin.ModelAdmin):
    list_display = ['friender', 'friended']
    class Meta:
        model = UserCloseFriendRelation()

admin.site.register(User, UserAccountAdmin)
admin.site.register(UserCloseFriendRelation, CloseFriendAdmin)
